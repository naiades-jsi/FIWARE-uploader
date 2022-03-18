import json

# Attirbutes in templates are alphabetically ordered

alert_template = {
    "alertSource":{
        "type": "Text",
        # Value will be added
    },
    "category": {
        "type": "Text",
        "value": "anomaly"
    },
    "dateIssued": {
        "type": "DateTime",
        # eg. "value": "2017-01-02T09:25:55.00Z"
    },
    "description": {
        "type": "Text",
        "value": "Final leakage position detected"
    },
    "location": {
        "type": "geo:json",
        "value": {
            "type": "Point",
            "coordinates": [ # to be inserted
            ]
        }
    },
    "subCategory": {
        "type": "Text",
        "value": "longTerm"
    },
    "type": "Alert",
    # Attributes that get updated 
    "updatedAttributes": {
        "type": "Text", 
        "value": "dateIssued,ksiSignature"
    } 
}

leakage_alert_template = {
    "alertSource":{
        "type": "Text",
        # Value will be added
    },
    "category": {
        "type": "Text",
        "value": "anomaly"
    },
    "dateIssued": {
        "type": "DateTime",
        # eg. "value": "2017-01-02T09:25:55.00Z"
    },
    "description": {
        "type": "Text"
        # Value will be added
    },
    "location": {
        "type": "geo:json",
        "value": {
            "type": "Point",
            "coordinates": [ # to be inserted
            ]
        }
    },
    "subCategory": {
        "type": "Text",
        "value": "longTerm"
    },
    "type": "Alert",
    # Attributes that get updated 
    "updatedAttributes": {
        "type": "Text", 
        "value": "dateIssued,description,ksiSignature"
    } 
}

consumption_template = {
    "category": {
        "type": "Text",
        "value": "water",
        "metadata": {}
    },
    "consumption": {
        "type": "Number",
        "value": None,
        "metadata": {},
    },
    "consumptionFrom": {
        "type": "DateTime",
        "dateFrom": "",
        "metadata": {}
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
    "consumptionTo": {
        "type": "DateTime",
        "dateTo": "",
        "metadata": {}
    },
    "consumptionUnit": {
        "type": "Text",
        "value": "m3/s",
        "metadata": {}
    },
    "dateCreated": {
        "type": "DateTime",
        "value": "",
        "metadata": {}
    },
    "subCategory": {
        "type": "Text",
        "value": "water-consumptiopn-prediction",
        "metadata": {}
    },
    "type": "Consumption",
    # Attributes that get updated 
    "updatedAttributes": {
        "type": "Text", 
        "value": "consumption,ksiSignature"
    } 
}

flower_bed_template = {
#    "feedbackDate": {
#        "type": "DateTime",
#        "value": ""
#    },
    "feedbackDescription": {
        "type": "Text",
        "value": ""
    },
    "nextWateringAmountRecommendation": {
        "type": "Number",
        "value": 0.5
    },
    "nextWateringDeadline": {
        "type": "DateTime",
        "value": "2017-03-31T08:00"
    },
    "type": "FlowerBed",
    # Attributes that get updated 
    "updatedAttributes": {
        "type": "Text", 
        "value": "feedbackDate,feedbackDescription,nextWateringAmountRecommendation,nextWateringDeadline,ksiSignature"
    } 
}

leakage_group_model_template = {
    "category": {
        "type" : "enum",
        "value": "water"
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
    },
    "subCategory": {
        "type" : "enum",
        "value": "leakage"
    },
    "type": "Alert",
    # Attributes that get updated 
    "updatedAttributes": {
        "type": "Text",
        "value": "data,dateIssued,ksiSignature"
    } 
}

leakage_model_template = {
    "isMovedToNewLocation":  {
        "type": "Boolean",
        "value": False
    },
    "type": "Device",
    # Attributes that get updated 
    "updatedAttributes": {
        "type": "Text", 
        "value": "isMovedToNewLocation,ksiSignature"
    } 
}

meta_signal_template = {
    "areaServed": {
        "type": "Text",
        "value": ""
    },
    "controlledProperty": {
        "type": "Text",
        "value": "flow"
    },
    "dateObserved": {
        "type": "datetime"
        # Value will be added
    },
    "description": {
        "type": "Text",
        "value": ""
    },
    "deviceType": {
        "type": "Text",
        "value": "sensor"
    },
    "location": {
        "type": "Point",
        "coordinates": [
            None,
            None
        ]
    },
    "measurementType": {
        "type": "Text",
        "value": None
    },
    "name": {
        "type": "Text",
        "value": ""
    },
    "numValue": {
        "type": "Number"
        # Value will be added
    },
    "outlier":  {
        "type": "Boolean",
        "value": False,
        "metadata": {}
    },
    "owner": [],
    "refDevice": {
        "type": "Text",
        "value": None
    },
    "seeAlso": [],   
    "textValue": {
        "type": "Text",
        "value": ""
    },
    "type": "DeviceMeasurement",    
    "unit": None,
    # Attributes that get updated 
    "updatedAttributes": {
        "type": "Text", 
        "value": "dateObserved,ksiSignature,numValue,textValue"
    } 
}