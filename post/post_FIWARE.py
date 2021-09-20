import requests
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




    def __init__(self, config, config_influx = None):
        self.type = config['type']['name']
        self.time_name = config['type']['time_name']
        self.data_name = config['type']['data_name']

        self.topics = config['kafka']['topics']
        self.consumer = KafkaConsumer(bootstrap_servers=config['kafka']['bootstrap_servers'], auto_offset_reset=config['kafka']['offset'])
        self.consumer.subscribe(self.topics)

        self.headers = config['fiware']['headers']
        self.url = config['fiware']['url']
        self.id = config['fiware']['id']
        self.sensor_name_re = config['fiware']['sensor_name_re']
        self.update = config['fiware']['update']

        # for influx
        if config_influx != None:
            self.influx  = PushToDB(url=config_influx["url"], token=config_influx["token"], org=config_influx["org"] )
            self.config_influx = config_influx


    def send(self):
        for msg in self.consumer:
            try:
                if self.type == 'consumption':
                    self.consumption(msg)
                elif self.type == 'leakage':
                    self.leakage(msg)
                elif self.type == 'leakage_position':
                    self.leakage_position(msg)
                elif self.type == 'flower_bed':
                    self.flower_bed(msg)
                elif self.type == "anomaly":
                    self.anomaly(msg)
                else :
                    print('Wrong type name.')
            except Exception as e:
                print(e)
                print('Did not send successfully.')
            #return 0

    def consumption(self, msg):
        rec = json.loads(msg.value.decode('utf-8'))

        timestamp = int(int(rec[self.time_name]) / 1000) # itmestamp in seconds

        topic = msg.topic # topic name
        #topic = msg["topic"]
        value = rec['value'] # extract value from record
        sensor_name = re.findall(self.sensor_name_re, topic)[0] # extract sensor from topic name
        
        data_model = copy.deepcopy(consumption_template) # create data_model

        # time
        time_stamp = datetime.utcfromtimestamp(timestamp) 

        horizon = int(rec['horizon'] / 24) + 'd'
        # data model
        entity_id = self.id + sensor_name + '_' + horizon # + time_stamp.strftime("%Y%m%d")

        # TODO during winter time it needs to be +1
        data_model['dateCreated']['value'] = (time_stamp).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + '.00Z+02' # +2 ali +1
        data_model['consumptionFrom']['value'] = (time_stamp + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + '.00Z+02'
        data_model['consumptionTo']['value'] = (time_stamp + timedelta(days=2)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + '.00Z+02'

        data_model['consumption']['value'] = value
        #data_model['consumptionMax'] = None
        #data_model['consumptionMin'] = None
        
        data_model['consumptionUnit'] = "m3/s"

        self.postToFiware(data_model, entity_id)

        #influx
        if self.config_influx != None:
            measurement = sensor_name
            # TODO timestamp should probably be in nanoseconds
            point = self.influx.create_point(measurement=measurement, time=datetime.fromtimestamp(timestamp), tags= {"horizont": horizon}, fields={'prediction': value} )
            if "alicante" in topic:
                self.influx.push_data(point=point, bucket = 'alicante_forecasting' )
            elif "braila" in topic:
                self.influx.push_data(point=point, bucket = 'braila_forecasting' )

    def anomaly(self, msg):
        rec = eval(msg.value) # kafka record
        # NOTE: we assume the timestamp is in ms
        timestamp = int(int(rec[self.time_name]) / 1000) # timestamp in seconds
        timestamp_in_ns = int(rec[self.time_name]) * 1000
        topic = msg.topic # topic name

        value = rec[self.data_name] # extract value from record
        sensor_name = re.findall(self.sensor_name_re, topic)[0] # extract sensor from topic name
        
        data_model = copy.deepcopy(alert_template) # create data_model

        entity_id = self.id + sensor_name
        dic = {
            -1 : "Error",
            0 : "Warning",
            1 : "OK",
            2 : "Undefined"
        }

        # time
        time_stamp = datetime.utcfromtimestamp(timestamp)
        if "pressure" in topic:
            data_model["subCategory"]["value"] = "long_term"
        elif "flow" in topic:
            data_model["subCategory"]["value"] = "long_term"

        data_model['description']['value'] = dic[int(rec['status_code'])]
        # TODO during winter time it needs to be +1
        data_model['dateIssued']['value'] = (time_stamp).isoformat() + '.00Z+02'

        data_model['validFrom']['value'] = (time_stamp).isoformat() + '.00Z+02'

        self.postToFiware(data_model, entity_id)

        #influx
        if self.config_influx != None:
            measurement = sensor_name
            
            output_dict = {'algorithm': rec["algorithm"],
                            "value": rec["value"],
                            "status": rec["status"],
                            "status_code": rec["status_code"]}
            if("suggested_value" in rec):
                output_dict["suggested_value"] = rec["suggested_value"]
            

            point = self.influx.create_point(measurement=measurement,
                                             time=timestamp_in_ns,
                                             tags= {},
                                             fields= output_dict)
            if "alicante" in topic:
                self.influx.push_data(point=point, bucket = 'alicante_anomaly' )
            elif "braila" in topic:
                self.influx.push_data(point=point, bucket = 'braila_forecasting' )
        

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
        data_model["dateIssued"]["value"] = (time_stamp).replace(microsecond=0).isoformat() + '.00Z+02'

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
        data_model["nextWateringAmountRecommendation"]['type'] = 'Number'
        data_model["nextWateringAmountRecommendation"]['value'] = rec['WA']

        data_model["nextWateringDeadline"]["type"] = "DateTime"
        data_model["nextWateringDeadline"]["value"] = rec['T'] + '.00Z+02'

        entity_id = self.id + sensor_name 

        self.postToFiware(data_model, entity_id)

    def postToFiware(self, data_model, entity_id):
        params = (
            ('options', 'keyValues'),
        )
        if self.update:
            dm_type = data_model["type"]
            data_model.pop("type")

            response = requests.post(self.url + entity_id + "/attrs/" , headers=self.headers, params=params, data=json.dumps(data_model) )
            #print(response.status_code, response.content)
            
            if response.status_code > 300:
                data_model["type"] = dm_type
                data_model['id'] = entity_id
                #print(self.url, entity_id, "\n")
                response = requests.post(self.url , headers=self.headers, params=params, data=json.dumps(data_model) )

        else:
            data_model['id'] = entity_id
            response = requests.post(self.url , headers=self.headers, params=params, data=json.dumps(data_model) )

        print(response.status_code, response.content)
