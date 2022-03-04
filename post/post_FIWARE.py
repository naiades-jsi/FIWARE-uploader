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

import json

from kafka import KafkaConsumer
from kafka import KafkaProducer

from create_data_models import meta_signal_template, consumption_template,\
    alert_template, flower_bed_template, leakage_model_template,\
    leakage_group_model_template
from custom_error import Custom_error    

from pushToInflux import PushToDB

class SendData():
    type: str
    time_name: str
    time_format: str
    locations: List[str]
    
    topics: List[str]
    consumer: Any

    headers: Dict[str, str]
    url: str
    id: str
    sensor_name_re: str
    update: bool

    influx: Any
    config_influx: Dict[str, str]

    API_user: str
    API_pass: str

    def __init__(self, config, config_influx = None):
        self.type = config["name"]
        self.time_name = config["time_name"]
        self.time_format = config["time_format"]

        if("locations" in config):
            self.locations = config["locations"]

        # Check if format is is acceptable
        if(self.time_format != "s" and self.time_format != "ms" and
           self.time_format != "ns" and self.time_format != "us"):
           print("Invalid unix_time_format at %s.", self.measurement,
                 flush=True)
           exit(1)

        self.topics = config["kafka"]["topics"]
        self.consumer = KafkaConsumer(bootstrap_servers=config["kafka"]["bootstrap_servers"], auto_offset_reset=config["kafka"]["offset"])
        self.consumer.subscribe(self.topics)

        self.headers = config["fiware"]["headers"]
        self.url = config["fiware"]["url"]
        self.id = config["fiware"]["id"]
        self.sensor_name_re = config["fiware"]["sensor_name_re"]
        self.update = config["fiware"]["update"]

        # KSI signature
        self.API_user = config["api_user"]
        self.API_pass = config["api_pass"]

        # for influx
        if config_influx != None:
            self.influx  = PushToDB(url=config_influx["url"], token=config_influx["token"], org=config_influx["org"] )
            self.config_influx = config_influx
        else:
            self.config_influx = None

        print("{} => configuration finished".format(datetime.now()), flush=True)

    def send(self):
        print("{} => started listening".format(datetime.now()), flush=True)
        for msg in self.consumer:
            print("{} => message recieved".format(datetime.now()), flush=True)
            try:
                if self.type == "consumption":
                    self.consumption(msg)
                elif self.type == "leakage_group":
                    self.leakage_group(msg)
                elif self.type == "leakage_position":
                    self.leakage_position(msg)
                elif self.type == "flower_bed":
                    self.flower_bed(msg)
                elif self.type == "anomaly":
                    self.anomaly(msg)
                elif self.type == "meta_signal":
                    self.meta_signal(msg)
                else :
                    print("Wrong type name.", flush=True)
            except Exception as e:
                print(e, flush=True)
                print("Did not send successfully.", flush=True)

    def consumption(self, msg):
        # TODO: add signature
        # sample output: {"timestamp": "2021-10-11 11:38:47.374354", "value": "[0.36906925]", "horizon": "24"}
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
        value = rec["value"][0]
        horizon = str(int(int(rec["horizon"]) / 24)) + "d" # Horizon is expected in hours
        prediction_time = int(rec["prediction_time"]/1000) # Must be in miliseconds
        from_time = timestamp_in_ns/1000000000
        to_time = from_time + int(rec["horizon"]) * 3600
        sensor_name = re.findall(self.sensor_name_re, topic)[0] # extract sensor from topic name

        # time
        prediction_time_timestamp = datetime.utcfromtimestamp(prediction_time)
        from_time_timestamp = datetime.utcfromtimestamp(from_time)
        to_time_timestamp = datetime.utcfromtimestamp(to_time)

        # data model
        data_model = copy.deepcopy(consumption_template) # create data_model
        entity_id = self.id + sensor_name + "_" + str(horizon) # + time_stamp.strftime("%Y%m%d")
        print(entity_id)
        # TODO during winter time it needs to be +1
        data_model["dateCreated"]["value"] = (prediction_time_timestamp).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + ".00Z+02" # +2 ali +1
        data_model["consumptionFrom"]["value"] = (from_time_timestamp).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + ".00Z+02"
        data_model["consumptionTo"]["value"] = (to_time_timestamp).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + ".00Z+02"

        data_model["consumption"]["value"] = value
        #data_model["consumptionMax"] = None
        #data_model["consumptionMin"] = None

        self.postToFiware(data_model, entity_id)

        #influx
        if self.config_influx != None:
            measurement = sensor_name
            prediction_time_in_ns = prediction_time * 1000000000

            output_dict = { "value": value }
            
            # Select bucket
            if "alicante" in topic:
                bucket = "alicante_forecasting" 
            elif "braila" in topic:
                bucket = "braila_forecasting"

            self.influx.write_data(measurement=measurement,
                                   timestamp=prediction_time_in_ns,
                                   tags= {},
                                   to_write= output_dict,
                                   bucket=bucket)

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
        data_model = copy.deepcopy(alert_template) # create data_model      

        
        """if "pressure" in topic:
            data_model["subCategory"]["value"] = "long_term"
        elif "flow" in topic:
            data_model["subCategory"]["value"] = "long_term"""

        data_model["description"]["value"] = rec["status"]
        data_model["alertSource"]["value"] = sensor_name
        # TODO during winter time it needs to be +1
        data_model["dateIssued"]["value"] = (time_stamp).isoformat() + ".00Z+02"
        # optional and unnecessary since it is the same as above
        # data_model["validFrom"]["value"] = (time_stamp).isoformat() + ".00Z+02"

        # Add location
        index = self.topics.index(topic)
        data_model["location"]["value"]["coordinates"] = self.locations[index]

        # Sign and append signature
        data_model = self.sign(data_model)

        self.postToFiware(data_model, entity_id)

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
        data_model = copy.deepcopy(meta_signal_template) # create data_model      

        #TODO set values of the data model
        # dateObserved
        data_model["dateObserved"]["value"] = (time_stamp).isoformat() + ".00Z+02"

        # numValue
        data_model["numValue"]["value"] = rec["status_code"]

        # textValue (contains the actual sample value/array of values on 
        # which anomaly detection was executed)
        data_model["textValue"]["value"] = str(rec["value"])

        # Sign and append signature
        data_model = self.sign(data_model)

        self.postToFiware(data_model, entity_id)

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
        
        data_model = copy.deepcopy(leakage_group_model_template) # create data_model

        # time
        time_stamp = datetime.utcfromtimestamp(timestamp_in_ns/1000000000) 

        # We are exporting to only one entity
        entity_id = "urn:ngsi-ld:Alert:RO-Braila-leakageGroup"
        #print(entity_id)

        data_model["dateIssued"]["value"] = (time_stamp).isoformat() + ".00Z+02"

        data_model["data"]["value"]["affectedGroup"]["value"] = rec

        # Sign and append signature
        data_model = self.sign(data_model)

        self.postToFiware(data_model, entity_id)

        #TODO add influx do we need it?

    def leakage_position(self, msg):
        # TODO: test signature
        # jaka's component
        # sample data : { "timestamp": 12912903193912, "position": [ LAT, LNG ], "final_location": boolean }
        rec = eval(msg.value) # kafka record
        
        # Change timestamp to ns
        if(self.time_format == "s"):
            timestamp_in_ns = int(rec[self.time_name]*1000000000)
        elif(self.time_format == "ms"):
            timestamp_in_ns = int(rec[self.time_name]*1000000)
        elif(self.time_format == "us"):
            timestamp_in_ns = int(rec[self.time_name]*1000)
        
        topic = msg.topic # topic name

        sensor_name = re.findall(self.sensor_name_re, topic)[0] # extract sensor name from topic name
        position = rec["position"]
        final_location = rec["is_final"]
        
        data_model = copy.deepcopy(leakage_model_template) # create data_model
        if(final_location):
            data_model["finalLeackageLocation"] = {
                "type": "geo:json",
                "value": {
                    "type": "Point",
                    "coordinates": position
                }
            }
        else:
            data_model["newLocation"] = {
                "type": "geo:json",
                    "value": {
                    "type": "Point",
                    "coordinates": position
                }
            }
        
        entity_id = "urn:ngsi-ld:Device:Device-" + sensor_name

        # Sign and append signature
        data_model = self.sign(data_model)

        self.postToFiware(data_model, entity_id)
        #TODO influx?
    
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
        time_stamp = datetime.utcfromtimestamp(timestamp_in_ns/1000000000)

        sensor_name = re.findall(self.sensor_name_re, topic)[0]
        
        # Construct data model
        data_model = copy.deepcopy(flower_bed_template) # create data_model  

        data_model["nextWateringAmountRecommendation"]["value"] = rec["WA"]
        data_model["feedbackDescription"]["value"] = str(rec["predicted_profile"])
        data_model["feedbackDate"]["value"] = (time_stamp).isoformat() + ".00Z+02"

        time_string = rec["T"].split()[0] + "T" + rec["T"].split()[1] + ".00Z+02"
        data_model["nextWateringDeadline"]["value"] = time_string

        # Find the correct entity
        entity_mapper = {
            "0a7d": "urn:ngsi-ld:FlowerBed:FlowerBed-3",
            "1f10": "urn:ngsi-ld:FlowerBed:FlowerBed-3",
            "0a80": "urn:ngsi-ld:FlowerBed:FlowerBed-4",
            "1f06": "urn:ngsi-ld:FlowerBed:FlowerBed-4",
            "0a6a": "urn:ngsi-ld:FlowerBed:FlowerBed-5",
            "1efd": "urn:ngsi-ld:FlowerBed:FlowerBed-5",
            "0a83": "urn:ngsi-ld:FlowerBed:FlowerBed-6",
            "1eff": "urn:ngsi-ld:FlowerBed:FlowerBed-6",
            "0972": "urn:ngsi-ld:FlowerBed:FlowerBed-7",
            "1f02": "urn:ngsi-ld:FlowerBed:FlowerBed-7",
            "0a81": "urn:ngsi-ld:FlowerBed:FlowerBed-8",
            "1efe": "urn:ngsi-ld:FlowerBed:FlowerBed-8",
            "0a7c": "urn:ngsi-ld:FlowerBed:FlowerBed-1",
            "1f0d": "urn:ngsi-ld:FlowerBed:FlowerBed-1",
            "0a35": "urn:ngsi-ld:FlowerBed:FlowerBed-2",
            "1f08": "urn:ngsi-ld:FlowerBed:FlowerBed-2"
        }
        entity_id = entity_mapper[sensor_name]

        # Sign and append signature
        data_model = self.sign(data_model)

        self.postToFiware(data_model, entity_id)

        #influx
        if self.config_influx != None:
            measurement = sensor_name + "_watering"

            output_dict = {"watering_amount": rec["WA"]}
            
            timestamp_of_watering = int(time.mktime(datetime.strptime(rec["T"], "%Y-%m-%d %H:%M:%S").timetuple()))*1000000000
            
            if("suggested_value" in rec):
                output_dict["suggested_value"] = rec["suggested_value"]
            
            # Select bucket
            bucket = "carouge_watering"

            self.influx.write_data(measurement=measurement,
                                             timestamp=timestamp_of_watering,
                                             tags= {},
                                             to_write= output_dict,
                                             bucket=bucket)

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

    def sign(self, data_model):
        # Try signing the message with KSI tool (requires execution in
        # the dedicated container)
        try:
            signature = self.encode(data_model)
        except Exception as e:
            print(f"Signing failed", flush=True)
            signature = "null"
        
        # Add signature to the message
        data_model["ksiSignature"] = {
            "metadata": {},
            "type": "Text",
            "value": signature
        }

        return data_model

    def encode(self, output_dict):
        # Less prints
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
        assert int(verification) == True

        return encodedZip


# TODO test fail request