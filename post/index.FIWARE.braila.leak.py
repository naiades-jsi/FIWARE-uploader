from post_FIWARE import SendData

config_leak = {
    'type':{
        'name': 'cosumption',
        'time_name': 'timestamp',
        'data_name': ['value']
    },
    'kafka':{
        'topics': [
            "braila_leakage_groups"
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
        'id': 'AffectedGroup:Romania-Braila-',
        'sensor_name_re': 'braila_leakage_(groups)'
    }
}

braila_leakage = SendData(config_leak)

braila_leakage.send()
