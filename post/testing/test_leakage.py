from time import sleep
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

topic = "braila_leakage_position2182"
message = {
   "timestamp": 1638921110,
   "position": {1: [[ 1.5, 5.2 ]], 2: [[1.5, 5.2], [2, 4]]},
   "is_final": True
}
message = {
   "timestamp": 1638921110,
   "position": [45.2458676937, 27.9371631536],
   "is_final": False
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