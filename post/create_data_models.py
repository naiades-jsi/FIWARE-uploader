import json

alert_template = {
    #"id": "",
    "type": "Alert",
    "category": {
        "type": "Text",
        "value": "anomaly"
    },
    "subCategory": {
        "type": "Text",
        "value": "longTerm"
    },
    "description": {
        "type": "Text"
        # Value will be added
    },
    "dateIssued": {
        "type": "DateTime",
        # eg. "value": "2017-01-02T09:25:55.00Z"
    },
    "alertSource":{
        "type": "Text",
        # Value will be added
    },
    "location": {
        "type": "geo:json",
        "value": {
            "type": "Point",
            "coordinates": [ # to be inserted
            ]
        }
    }
}

consumption_template = {
    #"id": None,
    "type": "Consumption",
    "category": {
        "type": "Text",
        "value": "water",
        "metadata": {}
    },
    "subCategory": {
        "type": "Text",
        "value": "water-consumptiopn-prediction",
        "metadata": {}
    },
    "dateCreated": {
        "type": "DateTime",
        "value": "",
        "metadata": {}
    },
    "consumption": {
        "type": "Number",
        "value": None,
        "metadata": {},
    },
    "consumptionMax": {
        "type": "Number",
        "value": None,
        "metadata": {},
    },
    "consumptionMin": {
        "type": "Number",
        "value": None,
        "metadata": {},
    },
    "consumptionUnit": {
        "type": "Text",
        "value": "m3/s",
        "metadata": {}
    },
    "consumptionFrom": {
        "type": "DateTime",
        "dateFrom": "",
        "metadata": {}
    },
    "consumptionTo": {
        "type": "DateTime",
        "dateTo": "",
        "metadata": {}
    }
}

flower_bed_template = {
    #"id": "",
    "type": "FlowerBed",
    "nextWateringDeadline": {
        "type": "DateTime",
        "value": "2017-03-31T08:00"
    },
    "nextWateringAmountRecommendation": {
        "type": "Number",
        "value": 0.5
    },
    "feedback": {
        "type": "Text",
        "value": ""
    }
}

leakage_group_model_template = {
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

leakage_model_template = {
    "type": "Device",
    "isMovedToNewLocation":  {
        "type": "Boolean",
        "value": False,
        "metadata": {}
    }
}