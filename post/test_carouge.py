from time import sleep
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

topic = "device_1efd_pred_output"

message = {
    "WA": 5,
    "T": "2020-12-29 00:00:00",
    "timestamp": 1632743895000
}
array = [
    "2021-9-30 00:00:00",
    "2021-10-1 00:00:00",
    "2021-10-2 00:00:00",
    "2021-10-3 00:00:00",
    "2021-10-4 00:00:00",
    "2021-10-5 00:00:00",
    "2021-10-6 00:00:00",
    "2021-10-7 00:00:00",
    "2021-10-8 00:00:00",
    "2021-10-9 00:00:00"
]

for i in range(10):
    print(i)
    message["timestamp"] = message["timestamp"] + 60000
    message["WA"] = i
    message["T"] = array[i]
    producer.send(topic, value=message)
    sleep(60)