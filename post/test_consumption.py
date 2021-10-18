from time import sleep
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

topic = "predictions_alicante_alipark_flow"

message = {
    "timestamp": 1632743895000,
    "value": "[0.36906925]",
    "horizon": "24",
    "prediction_time": 1632743896000
}

for i in range(100):
    print(i)
    producer.send(topic, value=message)
    sleep(20)