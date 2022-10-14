from tempfile import _TemporaryFileWrapper
import requests
from typing import Any, List, Dict
from datetime import datetime
from datetime import timedelta
import random
import pandas as pd
import os
import copy
import re
import time
import base64
import subprocess
import logging

import json

from kafka import KafkaConsumer
from kafka import KafkaProducer

from create_data_models import meta_signal_template, consumption_template,\
    alert_template, flower_bed_template, leakage_model_template,\
    leakage_group_model_template, leakage_alert_template, alert_template_ld,\
    leakage_alert_template_ld, consumption_template_ld, leakage_group_model_template_ld,\
    leakage_model_template_ld, meta_signal_template_ld
from entity_mapper import entity_mapper_carouge
from custom_error import Custom_error

from pushToInflux import PushToDB

# logging
LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s", level=logging.INFO)

class SendData():
    debug: bool
    already_sent: List[str]

    name: str
    time_name: str
    time_format: str
    locations: List[str]

    topics: List[str]
    consumer: Any

    format: str
    context: str
    headers: Dict[str, str]
    get_headers: Dict[str, str]
    url: str
    create_url: str
    get_url: str
    id: str
    sensor_name_re: str

    influx: Any
    config_influx: Dict[str, str]

    API_user: str
    API_pass: str

    def __init__(self, config, config_influx = None):
        if("debug" in config):
            self.debug = config["debug"] # == "True"
        else:
            self.debug = False

        # a list of entities that were already sent to (entity might need to be created)
        # On first run of the entity upload do a GET to see if the entity exists - if not
        # create and then add it to the list
        self.already_sent =[]

        self.name = config["name"]
        self.time_name = config["time_name"]
        self.time_format = config["time_format"]

        # Consumption has a mask for different horizons
        if(self.name == "consumption"):
            self.mask = config["mask"]

        # Check if format is is acceptable
        if(self.time_format != "s" and self.time_format != "ms" and
           self.time_format != "ns" and self.time_format != "us"):
           print("Invalid unix_time_format at %s.", self.measurement,
                 flush=True)
           exit(1)

        # Kafka configuration
        self.topics = config["kafka"]["topics"]
        self.consumer = KafkaConsumer(bootstrap_servers=config["kafka"]["bootstrap_servers"], auto_offset_reset=config["kafka"]["offset"])
        self.consumer.subscribe(self.topics)
        print("Subscribed to the following topics: ", self.topics)

        #print(self.topics)

        # Locations configuration
        if("locations" in config):
            self.locations = config["locations"]
        else:
            self.locations = [[0,0]]*len(self.topics)

        # Fiware configuration
        if("format" in config["fiware"]):
            self.format = config["fiware"]["format"]
            if(self.format == "ld"):
                self.context = config["fiware"]["context"]
        else:
            self.format = "v2"
        self.headers = config["fiware"]["headers"]
        self.get_headers = config["fiware"]["get_headers"]
        self.url = config["fiware"]["url"]
        self.create_url = config["fiware"]["create_url"]
        self.get_url = config["fiware"]["get_url"]
        self.id = config["fiware"]["id"]
        self.sensor_name_re = config["fiware"]["sensor_name_re"]

        # KSI signature (username and pass required in encode function)
        self.API_user = config["api_user"]
        self.API_pass = config["api_pass"]

        # for influx
        if config_influx != None:
            self.influx  = PushToDB(url=config_influx["url"], token=config_influx["token"], org=config_influx["org"] )
            self.config_influx = config_influx
        else:
            self.config_influx = None

        LOGGER.info("configuration finished")

    def send(self):
        LOGGER.info("Started listening")
        for msg in self.consumer:
            LOGGER.info("Message recieved from {}".format(msg.topic))
            if(self.debug):
                # In debug mode no try (for more info on crashe)
                if self.name == "consumption":
                    self.consumption(msg)
                elif self.name == "leakage_group":
                    self.leakage_group(msg)
                elif self.name == "leakage_position":
                    self.leakage_position(msg)
                elif self.name == "flower_bed":
                    self.flower_bed(msg)
                elif self.name == "anomaly":
                    self.anomaly(msg)
                elif self.name == "meta_signal":
                    self.meta_signal(msg)
                else :
                    LOGGER.error("Wrong type name.")
            else:
                try:
                    if self.name == "consumption":
                        self.consumption(msg)
                    elif self.name == "leakage_group":
                        self.leakage_group(msg)
                    elif self.name == "leakage_position":
                        self.leakage_position(msg)
                    elif self.name == "flower_bed":
                        self.flower_bed(msg)
                    elif self.name == "anomaly":
                        self.anomaly(msg)
                    elif self.name == "meta_signal":
                        self.meta_signal(msg)
                    else :
                        LOGGER.error("Wrong type name.")
                except Exception as e:
                    LOGGER.error("Did not send successfully: %s", str(e))

    def consumption(self, msg):
        # sample output: {"timestamp": "2021-10-11 11:38:47.374354", "value": "[0.36906925]", "horizon": "24"}
        rec = eval(msg.value)
        topic = msg.topic # topic name

        LOGGER.info("Received data: %s", json.dumps(rec))

        # Change timestamp to ns
        if(self.time_format == "s"):
            timestamp_in_ns = int(rec[self.time_name]*1000000000)
        elif(self.time_format == "ms"):
            timestamp_in_ns = int(rec[self.time_name]*1000000)
        elif(self.time_format == "us"):
            timestamp_in_ns = int(rec[self.time_name]*1000)

        # extract value from record
        # value = eval(rec["value"])[0]
        # iterate through all the horizons in the mask
        for i in self.mask:
            #print(f"i: {i}")
            # Extract the corret value
            value = rec["value"][i]

            # calculate horizon in hours and convert it to the readable form
            horizon_in_h = (i+1)/2
            if(horizon_in_h>=24):
                horizon_str = str(int(horizon_in_h/24)) + "d"
            else:
                horizon_str = str(int(horizon_in_h)) + "h"

            sensor_name = re.findall(self.sensor_name_re, topic)[0] # extract sensor from topic name

            # Time
            prediction_time = int(rec["prediction_time"]) # Must be in seconds
            from_time = timestamp_in_ns/1000000000
            to_time = from_time + horizon_in_h * 3600
            # Cast time in seconds
            prediction_time_timestamp = datetime.utcfromtimestamp(int(prediction_time))
            from_time_timestamp = datetime.utcfromtimestamp(from_time)
            to_time_timestamp = datetime.utcfromtimestamp(to_time)

            # copy predefined data model
            # Select the correct format
            if(self.format == "ld"):
                data_model = copy.deepcopy(consumption_template_ld) # create data_model
            else:
                data_model = data_model = copy.deepcopy(consumption_template)

            # Construct the name of the entity
            entity_id = self.id + sensor_name + "_" + horizon_str # + time_stamp.strftime("%Y%m%d")
            # print(entity_id)

            # TODO during winter time it needs to be +1
            if(self.format == "v2"):
                data_model["dateCreated"]["value"] = (prediction_time_timestamp).replace(hour=0, minute=0, second=0, microsecond=0).isoformat("T", "seconds") + "Z" # +2 ali +1
                data_model["consumptionFrom"]["value"] = (from_time_timestamp).replace(hour=0, minute=0, second=0, microsecond=0).isoformat("T", "seconds") + "Z"
                data_model["consumptionTo"]["value"] = (to_time_timestamp).replace(hour=0, minute=0, second=0, microsecond=0).isoformat("T", "seconds") + "Z"
            elif(self.format == "ld"):
                data_model["dateCreated"]["value"] = {
                    "@type": "DateTime",
                    "@value": (prediction_time_timestamp).replace(hour=0, minute=0, second=0, microsecond=0).isoformat("T", "seconds") + "Z"
                }
                data_model["consumptionFrom"]["value"] = {
                    "@type": "DateTime",
                    "@value": (from_time_timestamp).replace(hour=0, minute=0, second=0, microsecond=0).isoformat("T", "seconds") + "Z"
                }
                data_model["consumptionTo"]["value"] = {
                    "@type": "DateTime",
                    "@value": (to_time_timestamp).replace(hour=0, minute=0, second=0, microsecond=0).isoformat("T", "seconds") + "Z"
                }
            else:
                LOGGER.error(f"Could not send because of unsuported format {self.format}.")

            data_model["consumption"]["value"] = value
            #data_model["consumptionMax"] = None
            #data_model["consumptionMin"] = None

            # Sign and append signature
            #data_model = self.sign(data_model)

            try:
                LOGGER.info("Posting to FIWARE: %s", entity_id)
                if(self.format == "ld"):
                    self.postToFiware_context_ld(data_model, entity_id)
                elif(self.format == "v2"):
                    self.postToFiware_context_v2(data_model, entity_id)
                else:
                    LOGGER.error(f"Could not send because of unsuported format {self.format}.")
            except:
                pass
                #print("{} => Failed sent".format(datetime.now()), flush=True)

            time.sleep(1)

        #influx
        if self.config_influx != None:
            measurement = sensor_name
            prediction_time_in_ns = prediction_time * 1000000000

            # TODO influx should also recieve data for every horizon
            output_dict = { "value": rec["value"][0] }

            # Select bucket
            if "alicante" in topic:
                bucket = "alicante_forecasting"
            elif "braila" in topic:
                bucket = "braila_forecasting"
            try:
                self.influx.write_data(measurement=measurement,
                                       timestamp=prediction_time_in_ns,
                                       tags= {},
                                       to_write= output_dict,
                                       bucket=bucket)
            except:
                pass

    def anomaly(self, msg):
        # Translate codes to string
        dic = {
            -1 : "Error",
            0 : "Warning",
            1 : "OK",
            2 : "Undefined"
        }

        topic = msg.topic # topic name
        rec = eval(msg.value) # kafka record
        if "alicante" in topic:
            city = "Alicante"
        elif "braila" in topic:
            city = "Braila"
        elif "Carouge" in topic:
            city = "Carouge"
        else:
            city = "unknown"

        # Change timestamp to ns
        if(self.time_format == "s"):
            timestamp_in_ns = int(rec[self.time_name]*1000000000)
        elif(self.time_format == "ms"):
            timestamp_in_ns = int(rec[self.time_name]*1000000)
        elif(self.time_format == "us"):
            timestamp_in_ns = int(rec[self.time_name]*1000)

        # time to datetime
        time_stamp = datetime.utcfromtimestamp(timestamp_in_ns/1000000000)

        sensor_name = re.findall(self.sensor_name_re, topic)[0] # extract sensor from topic name
        # Entity ID based on alert notification
        entity_id = self.id + city + "-" + sensor_name
        #print(entity_id)
        #print(entity_id)

        #print("{} => creating model".format(datetime.now()), flush=True)

        # CREATE DATA MODEL TO POST
        # Select the correct format
        if(self.format == "ld"):
            data_model = copy.deepcopy(alert_template_ld) # create data_model
        else:
            data_model = copy.deepcopy(alert_template) # create data_model


        """if "pressure" in topic:
            data_model["subCategory"]["value"] = "long_term"
        elif "flow" in topic:
            data_model["subCategory"]["value"] = "long_term"""

        data_model["description"]["value"] = rec["status"]
        data_model["alertSource"]["value"] = sensor_name
        if(self.format == "v2"):
            data_model["dateIssued"]["value"] = (time_stamp).isoformat("T", "seconds") + "Z"
        elif(self.format == "ld"):
            data_model["dateIssued"]["value"] = {
                "@type": "DateTime",
                "@value": (time_stamp).isoformat("T", "seconds") + "Z"
            }
        else:
            print(f"Could not send because of unsuported format {self.format}.")

        # Add location
        index = self.topics.index(topic)
        data_model["location"]["value"]["coordinates"] = self.locations[index]

        # Sign and append signature
        data_model = self.sign(data_model)

        if(self.format == "ld"):
            self.postToFiware_context_ld(data_model, entity_id)
        elif(self.format == "v2"):
            self.postToFiware_context_v2(data_model, entity_id)
        else:
            print(f"Could not send because of unsuported format {self.format}.")

        #influx
        if self.config_influx != None:
            measurement = sensor_name

            output_dict = { "value": float(rec["value"][0]),
                            "status_code": rec["status_code"],
                            "algorithm": rec["algorithm"],
                            "status": rec["status"]}

            if("suggested_value" in rec):
                output_dict["suggested_value"] = rec["suggested_value"]

            # Select bucket
            if "alicante" in topic:
                bucket = "alicante_anomaly"
            elif "braila" in topic:
                bucket = "braila_anomaly"
            #print(timestamp_in_ns, flush=True)
            self.influx.write_data(measurement=measurement,
                                             timestamp=timestamp_in_ns,
                                             tags= {},
                                             to_write= output_dict,
                                             bucket=bucket)

    def meta_signal(self, msg):
        topic = msg.topic # topic name
        rec = eval(msg.value) # kafka record

        # Change timestamp to ns
        if(self.time_format == "s"):
            timestamp_in_ns = int(rec[self.time_name]*1000000000)
        elif(self.time_format == "ms"):
            timestamp_in_ns = int(rec[self.time_name]*1000000)
        elif(self.time_format == "us"):
            timestamp_in_ns = int(rec[self.time_name]*1000)

        # time to datetime
        time_stamp = datetime.utcfromtimestamp(timestamp_in_ns/1000000000)

        sensor_name = re.findall(self.sensor_name_re, topic)[0] # extract sensor from topic name

        # Entity ID based on alert notification
        entity_id = self.id + sensor_name + "-MetaSignal"
        #print(entity_id)

        #print("{} => creating model".format(datetime.now()), flush=True)

        # CREATE DATA MODEL TO POST
        # Select the correct format
        if(self.format == "ld"):
            data_model = copy.deepcopy(meta_signal_template_ld) # create data_model
        else:
            data_model = copy.deepcopy(meta_signal_template) # create data_model

        #TODO set values of the data model
        # dateObserved
        if(self.format == "v2"):
            data_model["dateObserved"]["value"] = (time_stamp).isoformat("T", "seconds") + "Z"
        elif(self.format == "ld"):
            data_model["dateObserved"]["value"] = {
                "@type": "DateTime",
                "@value": (time_stamp).isoformat("T", "seconds") + "Z"
            }
        else:
            print(f"Could not send because of unsuported format {self.format}.")

        # numValue
        data_model["value"]["value"] = rec["status_code"]

        # textValue (contains the actual sample value/array of values on
        # which anomaly detection was executed)
        data_model["description"]["value"] = str(rec["value"])

        # Sign and append signature
        #data_model = self.sign(data_model)

        if(self.format == "ld"):
            self.postToFiware_context_ld(data_model, entity_id)
        elif(self.format == "v2"):
            self.postToFiware_context_v2(data_model, entity_id)
        else:
            print(f"Could not send because of unsuported format {self.format}.")

        #influx
        if self.config_influx != None:
            measurement = sensor_name

            output_dict = { "value": float(rec["value"][0]),
                            "status_code": rec["status_code"],
                            "algorithm": rec["algorithm"],
                            "status": rec["status"]}

            if("suggested_value" in rec):
                output_dict["suggested_value"] = rec["suggested_value"]

            # Select bucket
            if "alicante" in topic:
                bucket = "alicante_anomaly"
            elif "braila" in topic:
                bucket = "braila_anomaly"
            #print(timestamp_in_ns, flush=True)
            try:
                self.influx.write_data(measurement=measurement,
                                                timestamp=timestamp_in_ns,
                                                tags= {},
                                                to_write= output_dict,
                                                bucket=bucket)
            except:
                print("{} => Influx upload failed".format(datetime.now()), flush=True)

    def frequency(self, msg):
        rec = eval(msg.value)

        topic = msg.topic # topic name

        # Change timestamp to ns
        if(self.time_format == "s"):
            timestamp_in_ns = int(rec[self.time_name]*1000000000)
        elif(self.time_format == "ms"):
            timestamp_in_ns = int(rec[self.time_name]*1000000)
        elif(self.time_format == "us"):
            timestamp_in_ns = int(rec[self.time_name]*1000)

        # extract value from record
        # value = eval(rec["value"])[0]
        for i in self.mask:
            # Extract the corret value
            value = rec["value"][i]

            # Calculate horizon
            horizon_in_h = (i+1)/2
            if(horizon_in_h>=24):
                horizon_str = str(int(horizon_in_h/24)) + "d"
            else:
                horizon_str = str(int(horizon_in_h)) + "h"

            sensor_name = re.findall(self.sensor_name_re, topic)[0] # extract sensor from topic name

            # Time
            prediction_time = int(rec["prediction_time"]/1000) # Must be in miliseconds
            from_time = timestamp_in_ns/1000000000
            to_time = from_time + horizon_in_h * 3600
            prediction_time_timestamp = datetime.utcfromtimestamp(prediction_time)
            from_time_timestamp = datetime.utcfromtimestamp(from_time)
            to_time_timestamp = datetime.utcfromtimestamp(to_time)

            # copy predefined data model
            data_model = copy.deepcopy(consumption_template) # create data_model

            # Construct the name of the entity
            entity_id = self.id + sensor_name + "_" + horizon_str # + time_stamp.strftime("%Y%m%d")
            print(entity_id)

            # TODO during winter time it needs to be +1
            data_model["dateCreated"]["value"] = (prediction_time_timestamp).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + ".00Z" # +2 ali +1
            data_model["consumptionFrom"]["value"] = (from_time_timestamp).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + ".00Z"
            data_model["consumptionTo"]["value"] = (to_time_timestamp).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + ".00Z"

            data_model["consumption"]["value"] = value
            #data_model["consumptionMax"] = None
            #data_model["consumptionMin"] = None

            # Sign and append signature
            data_model = self.sign(data_model)

            self.postToFiware_context_v2(data_model, entity_id)

    def leakage_group(self, msg):
        # TODO: test signature
        # Leakage group (Zan) => uploads to alert
        rec = eval(msg.value) # kafka record

        # Change timestamp to ns
        if(self.time_format == "s"):
            timestamp_in_ns = int(rec[self.time_name]*1000000000)
        elif(self.time_format == "ms"):
            timestamp_in_ns = int(rec[self.time_name]*1000000)
        elif(self.time_format == "us"):
            timestamp_in_ns = int(rec[self.time_name]*1000)

        # Only one topic (braila_leakage_groups)
        #topic = msg.topic # topic name
        #sensor_name = re.findall(self.sensor_name_re, topic)[0] # extract sensor name from topic name


        # CREATE DATA MODEL TO POST
        # Select the correct format
        if(self.format == "ld"):
            data_model = copy.deepcopy(leakage_group_model_template_ld) # create data_model
        else:
            data_model = copy.deepcopy(leakage_group_model_template) # create data_model

        # time
        time_stamp = datetime.utcfromtimestamp(timestamp_in_ns/1000000000)

        # We are exporting to only one entity
        entity_id = "urn:ngsi-ld:Alert:RO-Braila-leakageGroup"
        #print(entity_id)

        if(self.format == "v2"):
            data_model["dateIssued"]["value"] = (time_stamp).isoformat() + "Z"
        elif(self.format == "ld"):
            data_model["dateIssued"]["value"] = {
                "@type": "DateTime",
                "@value": (time_stamp).isoformat() + "Z"
            }
        else:
            print(f"Could not send because of unsuported format {self.format}.")


        data_model["data"]["value"]["affectedGroup"]["value"] = rec

        # Sign and append signature
        # data_model = self.sign(data_model)

        if(self.format == "ld"):
            self.postToFiware_context_ld(data_model, entity_id)
        elif(self.format == "v2"):
            self.postToFiware_context_v2(data_model, entity_id)
        else:
            print(f"Could not send because of unsuported format {self.format}.")

        #TODO add influx do we need it?

    def leakage_position(self, msg):
        # TODO: test signature
        # jaka's component
        # sample data : { "timestamp": 12912903193912, "position": [ LAT, LNG ], "final_location": boolean }
        rec = json.loads(msg.value) # kafka record

        # Change timestamp to ns
        if(self.time_format == "s"):
            timestamp_in_ns = int(rec[self.time_name]*1000000000)
        elif(self.time_format == "ms"):
            timestamp_in_ns = int(rec[self.time_name]*1000000)
        elif(self.time_format == "us"):
            timestamp_in_ns = int(rec[self.time_name]*1000)

        topic = msg.topic # topic name

        # time to datetime
        time_stamp = datetime.utcfromtimestamp(int(timestamp_in_ns/1000000000))

        sensor_name = re.findall(self.sensor_name_re, topic)[0] # extract sensor name from topic name
        position = rec["position"]
        final_location = rec["is_final"] == "true"

        if(final_location):
            #print("final", flush=True)
            """data_model["finalLeackageLocation"] = {
                "type": "geo:json",
                "value": {
                    "type": "Point",
                    "coordinates": position
                }
            }"""


            # Select the correct format
            if(self.format == "ld"):
                alert = copy.deepcopy(leakage_alert_template_ld)
            else:
                alert = copy.deepcopy(leakage_alert_template)

            alert_id = self.id

            if(self.format == "v2"):
                alert["dateIssued"]["value"] = (time_stamp).isoformat("T", "seconds") + "Z"
            elif(self.format == "ld"):
                alert["dateIssued"]["value"] = {
                    "@type": "DateTime",
                    "@value": (time_stamp).isoformat("T", "seconds") + "Z"
                }
            else:
                print(f"Could not send because of unsuported format {self.format}.")

            #print(str(position).replace("'", ""), flush=True)
            alert["description"]["value"] = str(position).replace("'", "")

            # Needs to be none empty
            alert["location"]["value"]["coordinates"] = [0,0]

            # Sign and append signature
            #alert = self.sign(alert)

            if(self.format == "ld"):
                self.postToFiware_context_ld(alert, alert_id)
            elif(self.format == "v2"):
                self.postToFiware_context_v2(alert, alert_id)
            else:
                print(f"Could not send because of unsuported format {self.format}.")

        else:
            # Select the correct format
            if(self.format == "ld"):
                data_model = copy.deepcopy(leakage_model_template_ld) # create data_model
            else:
                data_model = copy.deepcopy(leakage_model_template) # create data_model

            # Add the new location information
            data_model["newLocation"]["value"]["coordinates"] = position

            entity_id = "urn:ngsi-ld:Noise:Noise-" + sensor_name

            # Choose the correct upload function according to the format
            if(self.format == "ld"):
                self.postToFiware_context_ld(data_model, entity_id)
            elif(self.format == "v2"):
                self.postToFiware_context_v2(data_model, entity_id)
            else:
                print(f"Could not send because of unsuported format {self.format}.")

    def flower_bed(self, msg):
        # TODO: test signature
        rec = eval(msg.value) # kafka record
        topic = msg.topic # topic name

        # Change timestamp to ns
        if(self.time_format == "s"):
            timestamp_in_ns = int(rec[self.time_name]*1000000000)
        elif(self.time_format == "ms"):
            timestamp_in_ns = int(rec[self.time_name]*1000000)
        elif(self.time_format == "us"):
            timestamp_in_ns = int(rec[self.time_name]*1000)

        # time to datetime
        time_stamp = datetime.utcfromtimestamp(int(timestamp_in_ns/1000000000))

        sensor_name = re.findall(self.sensor_name_re, topic)[0]

        # Construct data model
        # Select the correct format
        if(self.format == "ld"):
            data_model = copy.deepcopy(flower_bed_template_ld) # create data_model
        else:
            data_model = copy.deepcopy(flower_bed_template) # create data_model

        # If WA=-1 ignore fields WA and T (no need for watering) - upload only predictions
        if(float(rec["WA"])!=-1):
            data_model["nextWateringAmountRecommendation"]["value"] = float(rec["WA"])

            # formati time
            day_year_month = rec["T"].split()[0]
            year, month, day = day_year_month.split("-")
            month = month.zfill(2)
            day = day.zfill(2)
            time_string =  year + "-" + month + "-" + day + "T" + rec["T"].split()[1] + "Z"

            if(self.format == "v2"):
                data_model["nextWateringDeadline"]["value"] = time_string
            elif(self.format == "ld"):
                data_model["dateIssued"]["value"] = {
                    "@type": "DateTime",
                    "@value": time_string
                }
            else:
                print(f"Could not send because of unsuported format {self.format}.")
        # Else remove fields next watering deadline and nextWateringAmountRecommendation
        else:
            del data_model["nextWateringDeadline"]
            del data_model["nextWateringAmountRecommendation"]

        data_model["feedbackDescription"]["value"] = str(rec["predicted_profile"])

        #data_model["feedbackDescription"]["value"] = "test"
        #data_model["feedbackDate"]["value"] = (time_stamp).isoformat() + ".00Z+02"

        # The date will be read from metadata instead
        #data_model["feedbackDate"]["value"] = time_stamp
        #

        #time_string = rec["T"].split()[0] + "T" + rec["T"].split()[1] + ".00Z"
        # data_model["nextWateringDeadline"]["value"] = datetime.strptime(rec["T"], "%Y-%m-%d %H:%M:%S")

        # Find the correct entity
        entity_id = entity_mapper_carouge[sensor_name]

        # Sign and append signature
        #data_model = self.sign(data_model)

        if(self.format == "ld"):
            self.postToFiware_ld(data_model, entity_id)
        elif(self.format == "v2"):
            self.postToFiware_context_v2(data_model, entity_id)
        else:
            print(f"Could not send because of unsuported format {self.format}.")

        #influx (if WA!=-1 - no prediction)
        if self.config_influx != None and float(rec["WA"])!=-1:
            measurement = sensor_name + "_watering"

            output_dict = {"watering_amount": rec["WA"]}

            # timestamp_of_watering = int(time.mktime(datetime.strptime(rec["T"], "%Y-%m-%d %H:%M:%S").timetuple()))*1000000000
            timestamp_of_watering = rec["T"].split()[0] + "T" + rec["T"].split()[1] + ".00Z+02"

            if("suggested_value" in rec):
                output_dict["suggested_value"] = rec["suggested_value"]

            # Select bucket
            bucket = "carouge_watering"
            try:
                self.influx.write_data(measurement=measurement,
                                                timestamp=timestamp_of_watering,
                                                tags= {},
                                                to_write= output_dict,
                                                bucket=bucket)
            except:
                print("{} => Influx upload failed".format(datetime.now()), flush=True)

    def postToFiware(self, data_model, entity_id):
        params = (
            ("options", "keyValues"),
        )
        if self.update:
            dm_type = data_model["type"]
            data_model.pop("type")

            # Try sending it to already existing entity (url)
            response = requests.post(self.url + entity_id + "/attrs/" , headers=self.headers, params=params, data=json.dumps(data_model) )

            # Otherwise add type and id and create new entity
            if response.status_code > 300:
                data_model["type"] = dm_type
                data_model["id"] = entity_id
                # print(self.url, entity_id, "\n", flush=True)
                response = requests.post(self.url , headers=self.headers, params=params, data=json.dumps(data_model) )

        else:
            data_model["id"] = entity_id
            response = requests.post(self.url , headers=self.headers, params=params, data=json.dumps(data_model) )

        if (response.status_code > 300):
            raise Custom_error(f"Error sending to the API. Response stauts code: {response.status_code}")

    def postToFiware_newv2(self, data_model, entity_id):
        data_model["id"] = entity_id

        body = {
            "subscriptionId": self.subscriptionId,
            "data": [data_model]
        }

        # Sign message body
        body = self.sign(body)

        if(self.debug):
            print(print(json.dumps(body, indent=4, sort_keys=True)))

        response = requests.post(self.url, headers=self.headers, data=json.dumps(body) )


        if (response.status_code > 300):
            print(f"Error sending to the API. Response status conde {response.status_code}", flush=True)
        try:
            if(type(eval(response.content.decode("utf-8"))) is not str):
                status_code = eval(response.content.decode("utf-8")).get("status_code")
                # Test for errors and log them
                if (status_code > 300):
                    message = eval(response.content.decode("utf-8")).get("message")
                    print(f"Error sending to the API. Response status conde {status_code}", flush=True)
                    print(f"Response body content: {message}")
                    # raise Custom_error(f"Error sending to the API. Response stauts code: {response.status_code}")
        except:
            print(response.content)

    def postToFiware_ld(self, data_model, entity_id):
        # Body construction
        data_model["id"] = entity_id
        data_model["@context"] = [self.context]

        body = data_model

        # Sign message body
        body = self.sign(body)

        #if (self.debug):
        #    print(print(json.dumps(body, indent=4, sort_keys=True)))

        # URL contstruction
        url = self.url + entity_id + "/attrs"

        response = requests.post(url, headers=self.headers, data=json.dumps(body) )

        # TODO test if it failed because the entity is not yet created
        if (response.status_code == 301):
            # Create entity
            url = self.create_url
            response = requests.post(url, headers=self.headers, data=json.dumps(body) )

            # Check if creatin was sucesfull
            if (response.status_code > 300):
                LOGGER.error("Error creating an entity")

        # Check if upload was successful
        if (response.status_code > 300):
            LOGGER.error(f"Error sending to the API. Response status conde {response.status_code}")
        try:
            if(type(eval(response.content.decode("utf-8"))) is not str):
                status_code = eval(response.content.decode("utf-8")).get("status_code")
                # Test for errors and log them
                if (status_code > 300):
                    message = eval(response.content.decode("utf-8")).get("message")
                    LOGGER.error(f"Error sending to the API. Response status conde {status_code}")
                    LOGGER.error(f"Response body content: {message}")
                    # raise Custom_error(f"Error sending to the API. Response stauts code: {response.status_code}")
        except:
            LOGGER.exception(response.content)

    def postToFiware_context_v2(self, data_model, entity_id):
        body = data_model

        # Sign message body
        body = self.sign(body)

        # URL contstruction
        url = self.url + entity_id + "/attrs"

        if(self.debug):
            print(f"URL: {url}")
            print(print(json.dumps(body, indent=4, sort_keys=True)))

        # If this is the first upload since the rerun the entity might need to be created
        if(entity_id not in self.already_sent):
            complete_get_url = self.get_url + entity_id
            # Do a get to check if entity exists
            #print(complete_get_url)
            response = requests.get(complete_get_url, headers=self.get_headers)

            # If entity was not found do a post to create it.
            if(response.status_code == 404):
                # For entity creation fields id and type must be added
                body["id"] = entity_id
                body["type"] = self.get_type_from_id(entity_id)

                print("{}: Entity {} missing. Creating with the following structure:".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), entity_id))
                print(json.dumps(body, indent=4, sort_keys=True))

                # Risky operation therefore do not execute in debug mode
                if(not self.debug):
                    response = requests.post(self.create_url, headers=self.headers, data=json.dumps(body))

            else:
                response = requests.patch(url, headers=self.headers, data=json.dumps(body), timeout=10)

            self.already_sent.append(entity_id)
        else:
            response = requests.patch(url, headers=self.headers, data=json.dumps(body), timeout=10)

        # Check if upload was successful
        if (response.status_code > 300):
            print(f"Error sending to the API. Response status code {response.status_code}", flush=True)
        try:
            if(type(eval(response.content.decode("utf-8"))) is not str):
                status_code = eval(response.content.decode("utf-8")).get("status_code")
                # Test for errors and log them
                if (status_code > 300):
                    message = eval(response.content.decode("utf-8")).get("message")
                    print(f"Error sending to the API. Response status conde {status_code}", flush=True)
                    print(f"Response body content: {message}")
                    # raise Custom_error(f"Error sending to the API. Response stauts code: {response.status_code}")
        except:
            print(response.content)

    def postToFiware_context_ld(self, data_model, entity_id):
        # Add fields specific to LD format
        data_model["@context"] = [self.context]
        body = data_model

        # Sign message body
        body = self.sign(body)

        # URL contstruction
        url = self.url + entity_id + "/attrs"

        if(entity_id not in self.already_sent):
            complete_get_url = self.get_url + entity_id
            # Do a get to check if entity exists
            response = requests.get(complete_get_url, headers=self.get_headers)

            # If entity was not found do a post to create it.
            if (response.status_code == 404):
                # For entity creation fields id and type must be added
                body["id"] = entity_id
                body["type"] = self.get_type_from_id(entity_id)

                url = self.create_url

                LOGGER.info("Entity {} missing. Creating with the following structure:".format(entity_id))
                LOGGER.info("URL: %s", url)
                LOGGER.info("Headers: %s", json.dumps(self.headers, indent=4, sort_keys=True))
                LOGGER.info("BODY: %s", json.dumps(body, indent=4, sort_keys=True))

                # Risky operation therefore do not execute in debug mode
                response = requests.post(url, headers=self.headers, data=json.dumps(body))

            # else POST to context broker
            else:
                # For entity update fields id and type must be added
                body["id"] = entity_id
                body["type"] = self.get_type_from_id(entity_id)

                LOGGER.info(f"headers: {self.headers}")
                LOGGER.info(f"URL: {url}")
                LOGGER.info(f"body: {json.dumps(body, indent=4, sort_keys=True)}")
                response = requests.post(url, headers=self.headers, data=json.dumps(body))

            self.already_sent.append(entity_id)
        else:
            # For entity update fields id and type must be added
            # this is needed for noise sensors (at least)
            body["id"] = entity_id
            body["type"] = self.get_type_from_id(entity_id)

            LOGGER.info(f"headers: {self.headers}")
            LOGGER.info(f"URL: {url}")
            LOGGER.info(f"body: {json.dumps(body, indent=4, sort_keys=True)}")
            response = requests.post(url, headers=self.headers, data=json.dumps(body))
            pass

        LOGGER.info(response.content)

        # Check if upload was successful
        if (response.status_code > 300):
            LOGGER.error(f"Error sending to the API. Response status conde {response.status_code}")
            try:
                if(type(eval(response.content.decode("utf-8"))) is not str):
                    status_code = eval(response.content.decode("utf-8")).get("status_code")
                    # Test for errors and log them
                    if (status_code > 300):
                        message = eval(response.content.decode("utf-8")).get("message")
                        LOGGER.error(f"Error sending to the API. Response status code {status_code}")
                        LOGGER.info(f"Response body content: {message}")
                        # raise Custom_error(f"Error sending to the API. Response stauts code: {response.status_code}")
            except:
                LOGGER.error(response.content)

    def postToFiware_ld(self, data_model, entity_id):
        # Body construction
        data_model["id"] = entity_id
        data_model["@context"] = [self.context]

        body = data_model

        # Sign message body
        body = self.sign(body)

        # URL contstruction
        url = self.url + entity_id + "/attrs"


        if(self.debug):
            print(f"URL: {url}")
            print(json.dumps(body, indent=4, sort_keys=True))

        response = requests.post(url, headers=self.headers, data=json.dumps(body) )

        # TODO test if it failed because the entity is not yet created
        if(response.status_code == 301):
            # Create entity
            url = self.create_url
            response = requests.post(url, headers=self.headers, data=json.dumps(body) )

            # Check if creatin was sucesfull
            if (response.status_code > 300):
                print(f"Error creating an entity", flush=True)

        # Check if upload was successful
        if (response.status_code > 300):
            print(f"Error sending to the API. Response status conde {response.status_code}", flush=True)
        try:
            if(type(eval(response.content.decode("utf-8"))) is not str):
                status_code = eval(response.content.decode("utf-8")).get("status_code")
                # Test for errors and log them
                if (status_code > 300):
                    message = eval(response.content.decode("utf-8")).get("message")
                    print(f"Error sending to the API. Response status conde {status_code}", flush=True)
                    print(f"Response body content: {message}")
                    # raise Custom_error(f"Error sending to the API. Response stauts code: {response.status_code}")
        except:
            print(response.content)

    def sign(self, data_model):
        """
        A Wraper that first obtains the KSI signature and then adds it
        to the message in the correct format
        """
        # Try signing the message with KSI tool (requires execution in
        # the dedicated container)
        try:
            signature = self.encode(data_model)
        except Exception as e:
            print(f"Signing failed", flush=True)
            signature = "signatureFailed"

        # Add signature to the message
        if(self.format == "v2"):
            data_model["ksiSignature"] = {
                "type": "Text",
                "metadata": {},
                "value": signature
            }
        else:
            data_model["ksiSignature"] = {
                "type": "Property",
                "value": signature
            }

        return data_model

    def encode(self, output_dict):
        """
        Code provided by the partners to first obtain the KSI signature
        (with the api_username and api_password from configuration) and
        then validate it
        """

        # Less prints (not to be mistaken for self.debug)
        debug = False

        # Transforms the JSON string ('dataJSON') to file (json.txt)
        os.system('echo %s > json.txt' %output_dict)
        #Sign the file using your credentials
        os.system(f'ksi sign -i json.txt -o json.txt.ksig -S http://5.53.108.232:8080 --aggr-user {self.API_user} --aggr-key {self.API_pass}')

        # get the signature
        with open("json.txt.ksig", "rb") as f:
            encodedZip = base64.b64encode(f.read())
            if debug:
                print(encodedZip.decode())

        # Checking if the signature is correct
        verification = subprocess.check_output(f'ksi verify -i json.txt.ksig -f json.txt -d --dump G -X http://5.53.108.232:8081 --ext-user {self.API_user} --ext-key {self.API_pass} -P http://verify.guardtime.com/ksi-publications.bin --cnstr E=publications@guardtime.com | grep -xq "    OK: No verification errors." ; echo $?', shell=True)

        # Raise error if it is not correctly signed
        # TODO once ksi is fixed change 1 to 0
        assert int(verification) == 1

        # Must return a decoded string
        return encodedZip.decode()

    def get_type_from_id(self, entity_id: str) -> str:
        """
        A function that extracts the entity type from it's id
        given that the format of is is urn:ngsi-ld:{entity_id}:...
        """
        type = entity_id.split(":")[2]

        if (type == "Consumption-Romania"):
            type = "WaterConsumption"

        return type