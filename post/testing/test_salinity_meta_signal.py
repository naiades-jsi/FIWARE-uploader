from time import sleep
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

topic = "anomalies_alicante_salinity_EA001_36_level_meta_signal"

message = {
    "algorithm": "Combination",
    "value": [4038.517],
    "status": "PercentScore",
    "timestamp": 1647989964879,
    "status_code": 0.00043859649122807013
    }

# http://naiades.simavi.ro:8668/v2/entities/urn:ngsi-ld:Device:RO-EA001_36_level-MetaSignal?lastN=10

for i in range(100):
    print(i)
    message["status_code"] += 0.01
    producer.send(topic, value=message)
    sleep(20)