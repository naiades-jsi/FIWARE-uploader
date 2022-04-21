from create_data_models import meta_signal_template, consumption_template,\
    alert_template, flower_bed_template, leakage_model_template,\
    leakage_group_model_template, leakage_alert_template

import copy
import requests
import json


def postToFiware(data_model, entity_id):
    headers = {
        "Fiware-Service": "braila",
        "Content-Type": "application/json"
    }
    params = (
        ("options", "keyValues"),
    )
    data_model["id"] = entity_id
    response = requests.post("http://5.53.108.182:1026/v2/entities/", headers=headers, params=params, data=json.dumps(data_model) )

    if (response.status_code > 300):
        raise Custom_error(f"Error sending to the API. Response stauts code: {response.status_code}")


data_model = copy.deepcopy(alert_template)
entity_name = "urn:ngsi-ld:Alert:RO-Braila-211106H360-state-analysis-tool"

data_model["description"]["value"] = "High pressure state"

postToFiware(data_model, entity_name)