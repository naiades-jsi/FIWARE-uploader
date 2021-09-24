import requests
from typing import Any, List, Dict
from datetime import datetime
from datetime import timedelta
import random
import pandas as pd
import copy
import re

import json

from kafka import KafkaConsumer
from kafka import KafkaProducer

from create_data_models import consumption_template, alert_template, flower_bed_template, leakage_model_template

from pushToInflux import PushToDB

class SendData():
    type: str
    time_name: str
    data_name: str
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


    def __init__(self, config, config_influx = None):
        self.type = config["type"]["name"]
        self.time_name = config["type"]["time_name"]
        self.data_name = config["type"]["data_name"]
        self.locations = config["type"]["locations"]

        self.topics = config["kafka"]["topics"]
        self.consumer = KafkaConsumer(bootstrap_servers=config["kafka"]["bootstrap_servers"], auto_offset_reset=config["kafka"]["offset"])
        self.consumer.subscribe(self.topics)

        self.headers = config["fiware"]["headers"]
        self.url = config["fiware"]["url"]
        self.id = config["fiware"]["id"]
        self.sensor_name_re = config["fiware"]["sensor_name_re"]
        self.update = config["fiware"]["update"]

        # for influx
        if config_influx != None:
            self.influx  = PushToDB(url=config_influx["url"], token=config_influx["token"], org=config_influx["org"] )
            self.config_influx = config_influx

        print("{} => configuration finished".format(datetime.now()), flush=True)


    def send(self):
        print("{} => started listening".format(datetime.now()), flush=True)
        for msg in self.consumer:
            print("{} => message recieved".format(datetime.now()), flush=True)
            try:
                if self.type == "consumption":
                    self.consumption(msg)
                elif self.type == "leakage":
                    self.leakage(msg)
                elif self.type == "leakage_position":
                    self.leakage_position(msg)
                elif self.type == "flower_bed":
                    self.flower_bed(msg)
                elif self.type == "anomaly":
                    self.anomaly(msg)
                else :
                    print("Wrong type name.", flush=True)
            except Exception as e:
                print(e, flush=True)
                print("Did not send successfully.", flush=True)
            #return 0

    def consumption(self, msg):
        rec = json.loads(msg.value.decode("utf-8"))

        timestamp = int(int(rec[self.time_name]) / 1000) # itmestamp in seconds

        topic = msg.topic # topic name
        #topic = msg["topic"]
        value = rec["value"] # extract value from record
        sensor_name = re.findall(self.sensor_name_re, topic)[0] # extract sensor from topic name
        
        data_model = copy.deepcopy(consumption_template) # create data_model

        # time
        time_stamp = datetime.utcfromtimestamp(timestamp) 

        horizon = int(rec["horizon"] / 24) + "d"
        # data model
        entity_id = self.id + sensor_name + "_" + horizon # + time_stamp.strftime("%Y%m%d")

        # TODO during winter time it needs to be +1
        data_model["dateCreated"]["value"] = (time_stamp).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + ".00Z+02" # +2 ali +1
        data_model["consumptionFrom"]["value"] = (time_stamp + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + ".00Z+02"
        data_model["consumptionTo"]["value"] = (time_stamp + timedelta(days=2)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + ".00Z+02"

        data_model["consumption"]["value"] = value
        #data_model["consumptionMax"] = None
        #data_model["consumptionMin"] = None
        
        data_model["consumptionUnit"] = "m3/s"

        self.postToFiware(data_model, entity_id)

        #influx
        if self.config_influx != None:
            measurement = sensor_name
            # TODO timestamp should probably be in nanoseconds
            point = self.influx.create_point(measurement=measurement, time=datetime.fromtimestamp(timestamp), tags= {"horizont": horizon}, fields={"prediction": value} )
            if "alicante" in topic:
                self.influx.push_data(point=point, bucket = "alicante_forecasting" )
            elif "braila" in topic:
                self.influx.push_data(point=point, bucket = "braila_forecasting" )

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
        # NOTE: we assume the timestamp is in ms
        timestamp = int(int(rec[self.time_name]) / 1000) # timestamp in seconds
        timestamp_in_ns = int(rec[self.time_name]) * 1000
        # time to datetime
        time_stamp = datetime.utcfromtimestamp(timestamp)
        day_of_month = f'{time_stamp.day:02d}'
        hour_of_day = f'{time_stamp.hour:02d}'
        
        sensor_name = re.findall(self.sensor_name_re, topic)[0] # extract sensor from topic name
        # Entity ID based on alert notification
        entity_id = self.id + city + "-" + sensor_name + "-" + day_of_month + '-' + hour_of_day
        #print(entity_id)

        #print("{} => creating model".format(datetime.now()), flush=True)

        # CREATE DATA MODEL TO POST
        data_model = copy.deepcopy(alert_template) # create data_model      

        
        """if "pressure" in topic:
            data_model["subCategory"]["value"] = "long_term"
        elif "flow" in topic:
            data_model["subCategory"]["value"] = "long_term"""

        data_model["description"]["value"] = dic[int(rec["status_code"])]
        data_model["alertSource"]["value"] = sensor_name
        # TODO during winter time it needs to be +1
        data_model["dateIssued"]["value"] = (time_stamp).isoformat() + ".00Z+02"
        # optional and unnecessary since it is the same as above
        # data_model["validFrom"]["value"] = (time_stamp).isoformat() + ".00Z+02"

        # Add location
        index = self.topics.index(topic)
        data_model["location"]["value"]["coordinates"] = self.locations[index]

        #print("{} => sending to fiware".format(datetime.now()), flush=True)

        self.postToFiware(data_model, entity_id)

        #influx
        if self.config_influx != None:
            measurement = sensor_name

            output_dict = { "value": rec["value"],
                            "status_code": rec["status_code"]}
            if("suggested_value" in rec):
                output_dict["suggested_value"] = rec["suggested_value"]
            
            # Select bucket
            if "alicante" in topic:
                bucket = "alicante_anomaly" 
            elif "braila" in topic:
                bucket = "braila_anomaly"

            point = self.influx.write_data(measurement=measurement,
                                             time=timestamp_in_ns,
                                             tags= {},
                                             to_write= output_dict,
                                             bucket=bucket)
            
        

    def leakage(self, msg):
        rec = eval(msg.value) # kafka record
        timestamp = int(rec[self.time_name] / 1000) # timestamp in seconds
        topic = msg.topic # topic name

        sensor_name = re.findall(self.sensor_name_re, topic)[0] # extract sensor name from topic name
        
        data_model = {} # create data_model

        data_model["type"] = "Alert"

        data_model["category"] = {
                "value": "water"
            }

        data_model["subCategory"] = {
                "value": "leakage"
            }

        # time
        time_stamp = datetime.utcfromtimestamp(timestamp) 

        entity_id = self.id + sensor_name
        data_model["dateIssued"]["type"] = "DateTime"
        data_model["dateIssued"]["value"] = (time_stamp).replace(microsecond=0).isoformat() + ".00Z+02"

        data_model["affectedGroup"]["type"] = "Array"
        data_model["affectedGroup"]["value"] = rec

        self.postToFiware(data_model, entity_id)

        #TODO add influx

    def leakage_position(self, msg):
        # TODO
        rec = eval(msg.value) # kafka record
        timestamp = int(rec[self.time_name] / 1000) # itmestamp in seconds
        topic = msg.topic # topic name

        sensor_name = re.findall(self.sensor_name_re, topic)[0] # extract sensor name from topic name
        data_model = {} # create data_model
    
    def flower_bed(self, msg):
        # TODO 
        rec = eval(msg.value) # kafka record
        timestamp = int(rec[self.time_name] / 1000) # itmestamp in seconds
        topic = msg.topic # topic name

        value = rec[self.data_name] # extract value from record

        sensor_name = re.findall(self.sensor_name_re, topic)[0]
        data_model = {}

        data_model["type"] = "FlowerBed"
        data_model["nextWateringAmountRecommendation"]["type"] = "Number"
        data_model["nextWateringAmountRecommendation"]["value"] = rec["WA"]

        data_model["nextWateringDeadline"]["type"] = "DateTime"
        data_model["nextWateringDeadline"]["value"] = rec["T"] + ".00Z+02"

        entity_id = self.id + sensor_name 

        self.postToFiware(data_model, entity_id)

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

        #print(response.status_code, response.content)
