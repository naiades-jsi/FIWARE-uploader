from time import sleep
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

topic = "braila_leakage_position2182"
# this message is not really working with the uploader
message = {
   "timestamp": 1638921110,
   "position": {1: [[45.2458676937, 27.9371631536]], 2: [[45.2458676937, 27.9371631536], [45.4458676937, 27.1371631536]]},
   "is_final": True
}

# this is the correct message for the uploader
message = {
   "timestamp": 1638921110,
   "position": [45.2458676937, 27.9371631536],
   "is_final": True
}

# urn:ngsi-ld:Alert:ES-Braila-Radunegru-FinaLekageLocation
#

"""{
   "timestamp": 12912903193912,
   "position": [ LAT, LNG ] / {1: [LAT, LONG], 2:[[LAT, LONG, LAT2, LONG2, LAT3, LONG3,...],[...]]},
   "is_final": boolean
}"""
for i in range(1):
    print(i)
    producer.send(topic, value=message)
    sleep(10)