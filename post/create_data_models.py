import json

# Attirbutes in templates are alphabetically ordered

alert_template = {
    "alertSource":{
        "type": "Text",
        "metadata": {}
        # Value will be added
    },
    "category": {
        "type": "Enum",
        "value": "water",
        "metadata": {}
    },
    "dateIssued": {
        "type": "DateTime",
        "metadata": {}
        # eg. "value": "2017-01-02T09:25:55.00Z"
    },
    "description": {
        "type": "Text",
        "value": "Final leakage position detected",
        "metadata": {}
    },
    "location": {
        "type": "geo:json",
        "value": {
            "type": "Point",
            "coordinates": [ # to be inserted
            ]
        },
        "metadata": {}
    },
    "subCategory": {
        "type": "Enum",
        "value": "ice",
        "metadata": {}
    },
    "type": "Alert"
    # Attributes that get updated 
    #updatedAttributes": {
    #    "type": "Text", 
    #    "value": "dateIssued,ksiSignature",
    #    "metadata": {}
    #} 
}

leakage_alert_template = {
    "alertSource":{
        "type": "Text",
        "metadata": {}
        # Value will be added
    },
    "category": {
        "type": "Text",
        "value": "anomaly",
        "metadata": {}
    },
    "dateIssued": {
        "type": "DateTime",
        "metadata": {}
        # eg. "value": "2017-01-02T09:25:55.00Z"
    },
    "description": {
        "type": "Text",
        "metadata": {}
        # Value will be added
    },
    "location": {
        "type": "geo:json",
        "value": {
            "type": "Point",
            "coordinates": [ # to be inserted
            ]
        },
        "metadata": {}
    },
    "type": "Alert"
    # Attributes that get updated 
    #"updatedAttributes": {
    #    "type": "Text", 
    #    "value": "dateIssued,description,ksiSignature",
    #    "metadata": {}
    #}
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
    "type": "Consumption"
    # Attributes that get updated 
    #"updatedAttributes": {
    #    "type": "Text", 
    #    "value": "consumption,dateCreated,consumptionFrom,consumptionTo,ksiSignature",
    #    "metadata": {}
    #}
}

flower_bed_template = {
    "feedbackDescription": {
        "type": "Text",
        "value": "",
        "metadata": {}
    },
    "nextWateringAmountRecommendation": {
        "type": "Number",
        "value": 0.5,
        "metadata": {}
    },
    "nextWateringDeadline": {
        "type": "DateTime",
        "value": "2017-03-31T08:00",
        "metadata": {}
    },
    "type": "FlowerBed"
    # Attributes that get updated 
    """"updatedAttributes": {
        "type": "Text", 
        "value": "feedbackDate,feedbackDescription,nextWateringAmountRecommendation,nextWateringDeadline,ksiSignature",
        "metadata": {}
    } """
}

leakage_group_model_template = {
    "category": {
        "type" : "enum",
        "value": "water",
        "metadata": {}
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
        },
        "metadata": {}
    },
    "dateIssued": {
        "type": "datetime",
        "value": "2017-01-02T09:25:55.00Z",
        "metadata": {}
    },
    "subCategory": {
        "type" : "enum",
        "value": "leakage",
        "metadata": {}
    },
    "type": "Alert"
    # Attributes that get updated 
    """"updatedAttributes": {
        "type": "Text",
        "value": "data,dateIssued,ksiSignature",
        "metadata": {}
    } """
}

leakage_model_template = {
    "isMovedToNewLocation":  {
        "type": "Boolean",
        "value": False,
        "metadata": {}
    },
    "type": "Device"
    # Attributes that get updated 
    """"updatedAttributes": {
        "type": "Text", 
        "value": "isMovedToNewLocation,ksiSignature",
        "metadata": {}
    } """
}

meta_signal_template = {
    "areaServed": {
        "type": "Text",
        "value": "",
        "metadata": {}
    },
    "controlledProperty": {
        "type": "Text",
        "value": "flow",
        "metadata": {}
    },
    "dateObserved": {
        "type": "Datetime",
        "metadata": {}
        # Value will be added
    },
    "description": {
        "type": "Text",
        "value": "",
        "metadata": {}
    },
    "deviceType": {
        "type": "Text",
        "value": "sensor",
        "metadata": {}
    },
    "location": {
        "type": "Point",
        "coordinates": [
            None,
            None
        ],
        "metadata": {}
    },
    "measurementType": {
        "type": "Text",
        "value": None,
        "metadata": {}
    },
    "name": {
        "type": "Text",
        "value": "",
        "metadata": {}
    },
    "numValue": {
        "type": "Number",
        "metadata": {}
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
        "value": None,
        "metadata": {}
    },
    "seeAlso": [],   
    "textValue": {
        "type": "Text",
        "value": "",
        "metadata": {}
    },
    "type": "DeviceMeasurement",    
    "unit": None
    # Attributes that get updated 
    #"updatedAttributes": {
    #    "type": "Text", 
    #    "value": "dateObserved,ksiSignature,numValue,textValue",
    #    "metadata": {}
    #}
}