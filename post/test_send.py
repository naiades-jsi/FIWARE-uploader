import requests
import json

url = "http://naiades.simavi.ro:1026/ngsi-ld/v1/entities/urn:ngsi-ld:Alert:RO-Braila-flow_211106H360/attrs"
#url = "http://naiades.simavi.ro:5002/validation/ld/entities/urn:ngsi-ld:Alert:RO-Braila-flow_211106H360/attrs"
headers = {'Fiware-Service': 'braila', 'Content-Type': 'application/ld+json'}
body = {
    "@context": [
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
    ],
    "alertSource": {
        "type": "Property",
        "value": "flow_211106H360"
    },
    "dateIssued": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": "2022-01-10T07:34:46Z"
        }
    },
    "description": {
        "type": "Property",
        "value": "Error: measurement above upper limit"
    },
    "ksiSignature": {
        "type": "Property",
        "value": "signatureFailed"
    },
    "location": {
        "type": "GeoProperty",
        "value": {
            "coordinates": [
                0,
                0
            ],
            "type": "Point"
        }
    },
    "updatedAttributes": {
        "type": "Property",
        "value": "alertSource,dateIssued,description,ksiSignature,location,updatedAttributes"
    }
}
p = requests.patch(url, headers=headers, data=json.dumps(body))
print(p.content)
print(p.status_code)