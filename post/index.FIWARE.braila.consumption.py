from post_FIWARE import SendData

config_bra = {
    'type':{
        'name': 'consumption',
        'time_name': 'stampm',
        'data_name': ['value']
    },
    'kafka':{
        'topics': [
            
            "predictions_braila_flow318505H498_prediction",
            "predictions_braila_flow211306H360_prediction",
            "predictions_braila_flow211106H360_prediction",
            "predictions_braila_flow211206H360_prediction"
            ],
        'bootstrap_servers': "localhost:9092",
        'offset':'earlist'
    },
    'fiware':{
        'headers': {
            'Fiware-Service': 'braila',
            'Content-Type': 'application/json',
        },
        'update': True,
        'url': 'http://5.53.108.182:1026/v2/entities/',
        'id': 'Consumption-Romania:Romania-Braila-',
        'sensor_name_re': 'predictions_braila_(flow.+)_prediction'
    }
}

influx_config = {
        "token" : "----INFLUX-TOKEN----------",
        "org" : "naiades",
        "url" : "http://atena.ijs.si:8086"
    }

braila_consumption = SendData(config_bra, config_influx=influx_config)

braila_consumption.send()

