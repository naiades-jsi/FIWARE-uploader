import json

# Attirbutes in templates are alphabetically ordered

alert_template = {
    "alertSource":{
        "type": "Text",
        "metadata": {}
        # Value will be added
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
    # Attributes that get updated
    "updatedAttributes": {
        "type": "Text",
        "value": "alertSource,dateIssued,description,ksiSignature,location,updatedAttributes",
        "metadata": {}
    }
}

leakage_alert_template = {
    #"alertSource":{
    #    "type": "Text",
    #    "metadata": {}
    #    # Value will be added
    #},
    #"category": {
    #    "type": "Enum",
    #    "value": "water",
    #    "metadata": {}
    #},
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
    # Attributes that get updated
    "updatedAttributes": {
        "type": "Text",
        "value": "dateIssued,description,ksiSignature,location,updatedAttributes",
        "metadata": {}
    }
}

consumption_template = {
    #"category": {
    #   "type": "Text",
    #    "value": "water",
    #    "metadata": {}
    #},
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
    # Attributes that get updated
    "updatedAttributes": {
        "type": "Text",
        "value": "consumption,dateCreated,consumptionFrom,consumptionTo,ksiSignature,updatedAttributes",
        "metadata": {}
    }
}

flower_bed_template = {
    "feedbackDescription": {
        "type": "Text",
        "value": "",
        "metadata": {}
    },
    "nextWateringAmountRecommendation": {
        "type": "Number",
        "value": 0,
        "metadata": {}
    },
    "nextWateringDeadline": {
        "type": "DateTime",
        "value": "",
        "metadata": {}
    },
    #Attributes that get updated
    "updatedAttributes": {
        "type": "Text",
        "value": "feedbackDescription,nextWateringAmountRecommendation,nextWateringDeadline,ksiSignature,updatedAttributes",
        "metadata": {}
    }
}

leakage_group_model_template = {
    "category": {
        "type": "Text",
        "value": "alert"
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
    #"subCategory": {
    #    "type" : "Enum",
    #    "value": "ice",
    #    "metadata": {}
    #},
    # Attributes that get updated
    "updatedAttributes": {
        "type": "Text",
        "value": "category,data,dateIssued,ksiSignature,updatedAttributes",
        "metadata": {}
    }
}

leakage_model_template = {
    "isMovedToNewLocation":  {
        "type": "Boolean",
        "value": "false",
        "metadata": {}
    },
    # Attributes that get updated
    "updatedAttributes": {
        "type": "Text",
        "value": "isMovedToNewLocation,ksiSignature,updatedAttributes",
        "metadata": {}
    }
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
    # Attributes that get updated
    "updatedAttributes": {
        "type": "Text",
        "value": "dateObserved,description,ksiSignature,value,updatedAttributes",
        "metadata": {}
    }
}

# LD TEMPLATES

alert_template_ld = {
    "alertSource":{
        "type": "Property"
        # Value will be added
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
    # Attributes that get updated
    "updatedAttributes": {
        "type": "Property",
        "value": "alertSource,dateIssued,description,ksiSignature,location,updatedAttributes"
    }
}
leakage_alert_template_ld = {
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
    # Attributes that get updated
    "updatedAttributes": {
        "type": "Property",
        "value": "category,dateIssued,description,ksiSignature,location,updatedAttributes"
    }
}

consumption_template_ld = {
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
    # Attributes that get updated
    "updatedAttributes": {
        "type": "Property",
        "value": "consumption,dateCreated,consumptionFrom,consumptionTo,ksiSignature,updatedAttributes"
    }
}

leakage_group_model_template_ld = {
    "category": {
        "metadata": {},
        "type": "Property",
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
    # Attributes that get updated
    "updatedAttributes": {
        "type": "Property",
        "value": "category,data,dateIssued,ksiSignature,updatedAttributes"
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
    # Attributes that get updated
    "updatedAttributes": {
        "type": "Property",
        "value": "isMovedToNewLocation,newLocation,ksiSignature,updatedAttributes"
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
    # Attributes that get updated
    "updatedAttributes": {
        "type": "Property",
        "value": "dateObserved,description,ksiSignature,value,updatedAttributes"
    }
}