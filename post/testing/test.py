import requests
import json
from datetime import datetime

def postToFiware(data_model, entity_id):
    update = True
    url = "http://5.53.108.182:1026/v2/entities/"
    headers =  {
                "Fiware-Service": "braila",
                "Content-Type": "application/json"
            }
    params = (
        ("options", "keyValues"),
    )
    if update:
        dm_type = data_model["type"]
        data_model.pop("type")

        # Try sending it to already existing entity (url)
        response = requests.post(url + entity_id + "/attrs/" , headers=headers, params=params, data=json.dumps(data_model) )

        # Otherwise add type and id and create new entity
        if response.status_code > 300:
            data_model["type"] = dm_type
            data_model["id"] = entity_id
            # print(self.url, entity_id, "\n", flush=True)
            response = requests.post(url , headers=headers, params=params, data=json.dumps(data_model) )

    else:
        data_model["id"] = entity_id
        response = requests.post(url , headers=headers, params=params, data=json.dumps(data_model) )
    print(response.status_code)

rec = {"timestamp": 1641718805, 
"timestamp-processed-at": 1640605191, 
"critical-sensor": "SenzorComunarzi-NatVech", 
"deviation": 38.089476916190385, 
"method": "jenks_natural_breaks", 
"epanet-file": "RaduNegru24May2021","data": [{"0": "Sensors reporting missing data: [SenzorComunarzi-NatVech]"}]}

"""rec = {"timestamp": 1640372416, 
"timestamp-processed-at": 1640605191, 
"critical-sensor": "SenzorComunarzi-NatVech", 
"deviation": 38.089476916190385, 
"method": "jenks_natural_breaks", 
"epanet-file": "RaduNegru24May2021", 
"data": [{"node-name": "760-A", "latitude": 45.24570092953181, "longitude": 27.941960170281554, "group": 0}]}"""

time_format = "s"
time_name = "timestamp"

# Change timestamp to ns
if(time_format == "s"):
    timestamp_in_ns = int(rec[time_name]*1000000000)
elif(time_format == "ms"):
    timestamp_in_ns = int(rec[time_name]*1000000)
elif(time_format == "us"):
    timestamp_in_ns = int(rec[time_name]*1000)

# Only one topic (braila_leakage_groups)
#topic = msg.topic # topic name
#sensor_name = re.findall(self.sensor_name_re, topic)[0] # extract sensor name from topic name

data_model = {
    #"id": "",
    "type": "Alert",
    "category": {
        "type" : "enum",
        "value": "water"
    },
    "subCategory": {
        "type" : "enum",
        "value": "leakage"
    },
    "data": {
        "type" : "structuredvalue",
        "value": {
            "affectedGroup": {
                "Type": "Array",
                "value": {
                    "0": [],
                    "1": []
                }
            }
        }
        
    },
    "dateIssued": {
        "type": "datetime",
        "value": "2017-01-02T09:25:55.00Z"
    }
}

# time
time_stamp = datetime.utcfromtimestamp(timestamp_in_ns/1000000000) 

# We are exporting to only one entity
entity_id = "urn:ngsi-ld:Alert:RO-Braila-leakageGroup"
#print(entity_id)

data_model["dateIssued"]["value"] = (time_stamp).isoformat() + ".00Z+02"

data_model["data"]["value"]["affectedGroup"]["value"] = rec

postToFiware(data_model, entity_id)