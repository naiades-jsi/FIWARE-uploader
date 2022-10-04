import requests
import json

data_model = {
    "alertSource": {
        "type": "StructuredValue",
        "value": {
            "type": "Text",
            "value": "test"
        }
    }
}

headers = {
    "Fiware-Service": "braila",
    "Content-Type": "application/json"
    }
params={}

r = requests.post("http://5.53.108.182:1026/v2/entities/urn:ngsi-ld:Alert:ES-Alert-Braila-pressure_5770-27-12/attrs/",
              headers=headers, params=params, data=json.dumps(data_model) )
print(r.status_code, r.content)