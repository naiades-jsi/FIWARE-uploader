from time import sleep
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

topic = "braila_leakage_position2182"

message = { 
   "timestamp": 1635167318000000,
   "position": [ 1.1, 2.2 ],
   "final_location": "false"
}

for i in range(100):
    print(i)
    producer.send(topic, value=message)
    sleep(30)