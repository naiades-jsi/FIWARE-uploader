from time import sleep
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

topic = "anomalies_alicante_salinity_EA001_36_level"

message = {
    "algorithm": "Border check",
    "value": [6120.0],
    "status": "Error: measurement above upper limit",
    "timestamp": 1638399536,
    "status_code": -1
}

for i in range(100):
    print(i)
    producer.send(topic, value=message)
    sleep(20)