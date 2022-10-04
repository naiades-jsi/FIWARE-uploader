from time import sleep
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

topic = "anomalies_braila_flow211106H360_meta_signal"
#topic="t"
message = {
    "algorithm": "Combination",
    "value": [6122.0],
    "status": "Percent score",
    "timestamp": 1641800086654,
    "status_code": 0.0
}
print(topic)
for i in range(100):
    print(i)
    producer.send(topic, value=message)
    sleep(15)
    