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
    #"alertSource":{
    #    "type": "Text",
    #    "metadata": {}
    #    # Value will be added
    #},
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
        "metadata": {},
    },
    "consumptionFrom": {
        "type": "DateTime",
        "metadata": {}
    },
    "consumptionTo": {
        "type": "DateTime",
        "metadata": {}
    },
    "dateCreated": {
        "type": "DateTime",
        "metadata": {}
    },
    "type": "WaterConsumption"
    # Attributes that get updated 
    #"updatedAttributes": {
    #    "type": "Property", 
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
        "value": "2017-03-31T08:00:00.00Z",
        "metadata": {}
    },
    "type": "FlowerBed"
    # Attributes that get updated 
    #"updatedAttributes": {
    #    "type": "Text", 
    #    "value": "feedbackDate,feedbackDescription,nextWateringAmountRecommendation,nextWateringDeadline,ksiSignature",
    #    "metadata": {}
    #} """
}

leakage_group_model_template = {
    "category": {
        "type" : "Enum",
        "value": "water",
        "metadata": {}
    },
    "data": {
        "type" : "StructuredValue",
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
        "type": "Datetime",
        "value": "2017-01-02T09:25:55.00Z",
        "metadata": {}
    },
    "subCategory": {
        "type" : "Enum",
        "value": "ice",
        "metadata": {}
    },
    "type": "Alert"
    # Attributes that get updated 
    #"updatedAttributes": {
    #    "type": "Text",
    #    "value": "data,dateIssued,ksiSignature",
    #    "metadata": {}
    #} """
}

leakage_model_template = {
    "isMovedToNewLocation":  {
        "type": "Boolean",
        "value": "false",
        "metadata": {}
    },
    "type": "Device",
    # Attributes that get updated 
    #"updatedAttributes": {
    ##    "type": "Text", 
    #    "value": "isMovedToNewLocation,ksiSignature",
    #    "metadata": {}
    #}
}

meta_signal_template = {
    "dateObserved": {
        "type": "DateTime",
        "metadata": {}
        # Value will be added
    },
    "description": {
        "type": "Text",
        "value": "",
        "metadata": {}
    },
    "value": {
        "type": "Number",
        "metadata": {}
        # Value will be added
    },
    #"seeAlso": [],
    "type": "Device"
    # Attributes that get updated 
    #"updatedAttributes": {
    #    "type": "Text", 
    #    "value": "dateObserved,description,ksiSignature,value",
    #    "metadata": {}
    #}
}

# LD TEMPLATES

alert_template_ld = {
    "alertSource":{
        "type": "Property"
        # Value will be added
    },
    "category": {
        "type": "Property",
        "value": "water"
    },
    "dateIssued": {
        "type": "Property"
        # eg. "value": "2017-01-02T09:25:55.00Z"
    },
    "description": {
        "type": "Property",
        "value": "Final leakage position detected"
    },
    "location": {
        "type": "GeoProperty",
        "value": {
            "type": "Point",
            "coordinates": [ # to be inserted
            ]
        }
    },
    "subCategory": {
        "type": "Propety",
        "value": "ice"
    },
    "type": "Alert",
    # Attributes that get updated 
    "updatedAttributes": {
        "type": "Property", 
        "value": "alertSource,dateIssued,description,ksiSignature"
    } 
}
leakage_alert_template_ld = {
    #"alertSource":{
    #    "type": "Property",
    #    "metadata": {}
    #    # Value will be added
    #},
    "category": {
        "type": "Property",
        "value": "water"
    },
    "dateIssued": {
        "type": "Property"
        # eg. "value": "2017-01-02T09:25:55.00Z"
    },
    "description": {
        "type": "Property"
        # Value will be added
    },
    "location": {
        "type": "GeoProperty",
        "value": {
            "type": "Point",
            "coordinates": [ # to be inserted
            ]
        }
    },
    "type": "Alert",
    # Attributes that get updated 
    "updatedAttributes": {
        "type": "Property", 
        "value": "dateIssued,description,ksiSignature"
    }
}

consumption_template_ld = {
    "category": {
        "type": "Property",
        "value": "water"
    },
    "consumption": {
        "type": "Property"
    },
    "consumptionFrom": {
        "type": "Property"
    },
    "consumptionTo": {
        "type": "Property"
    },
    "dateCreated": {
        "type": "Property"
    },
    "type": "WaterConsumption",
    # Attributes that get updated 
    "updatedAttributes": {
        "type": "Property", 
        "value": "consumption,dateCreated,consumptionFrom,consumptionTo,ksiSignature"
    }
}

leakage_group_model_template_ld = {
    "category": {
        "type" : "Property",
        "value": "water"
    },
    "data": {
        "type" : "Property",
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
        "type": "Property",
        "value": "2017-01-02T09:25:55.00Z"
    },
    "subCategory": {
        "type" : "Property",
        "value": "ice"
    },
    "type": "Alert",
    # Attributes that get updated 
    "updatedAttributes": {
        "type": "Property",
        "value": "data,dateIssued,ksiSignature"
    }
}

leakage_model_template_ld = {
    "isMovedToNewLocation":  {
        "type": "Property",
        "value": "false"
    },
    "newLocation": {
        "type": "GeoProperty",
        "value": {
            "type": "Point",
            "coordinates": []
        }
    },
    "type": "Device",
    # Attributes that get updated 
    "updatedAttributes": {
        "type": "Property", 
        "value": "isMovedToNewLocation,newLocation,ksiSignature"
    }
}

meta_signal_template_ld = {
    "dateObserved": {
        "type": "Property"
        # Value will be added
    },
    "description": {
        "type": "Property",
        "value": ""
    },
    "value": {
        "type": "Property"
        # Value will be added
    },
    #"seeAlso": [],
    "type": "Device",
    # Attributes that get updated 
    "updatedAttributes": {
        "type": "Property", 
        "value": "dateObserved,description,ksiSignature,value"
    }
}