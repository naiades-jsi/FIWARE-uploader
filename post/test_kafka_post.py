from time import sleep
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

topic = "anomalies_braila_pressure_5770"

message = {
    "algorithm": "alg1",
    "status_code": -1,
    "status": "Error",
    "suggested_value": 5,
    "value": 2,
    "timestamp": 1632383976000
}

for i in range(100):
    print(i)
    message["timestamp"] = message["timestamp"] + 60000
    message["value"] = i
    producer.send(topic, value=message)
    sleep(60)