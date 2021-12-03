from time import sleep
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

topic = "braila_leakage_groups"

message = {"timestamp": 1638522139, "data": {"0": ["763-A", "760-A", "751-A", "748-A", "Jonctiune-J-26", "246-B", "246-A", "Jonctiune-4706", "760-B", "242-B", "242-A", "245-B", "245-A", "244-B", "244-A", "243-A", "243-B", "251-B", "251-A", "Jonctiune-3422", "Jonctiune-J-25", "763-B", "Jonctiune-3386", "Jonctiune-2749", "Jonctiune-4615", "279-A", "279-B", "Jonctiune-3467", "Jonctiune-J-22", "Jonctiune-3425", "Jonctiune-J-1", "Jonctiune-J-27", "Jonctiune-2750", "Jonctiune-J-3", "Jonctiune-J-19", "Jonctiune-3956", "Jonctiune-J-32", "Jonctiune-2729", "256-A", "256-B", "Jonctiune-J-21", "257-B", "257-A", "197-A", "197-B", "255-A", "255-B", "Jonctiune-2202", "Jonctiune-2734", "280-B", "280-A", "Jonctiune-3074", "Jonctiune-3458", "Jonctiune-4723", "Jonctiune-3920", "Jonctiune-3446", "Jonctiune-2756", "Jonctiune-J-10", "Jonctiune-2208", "Jonctiune-3466", "Jonctiune-2751", "Jonctiune-2753", "Jonctiune-2911", "Jonctiune-3067", "Jonctiune-J-33", "Jonctiune-3917", "Jonctiune-2197", "Jonctiune-3448", "Jonctiune-2730", "Jonctiune-3460", "Jonctiune-2752", "Jonctiune-3461", "Jonctiune-3463", "Jonctiune-2774", "Jonctiune-1225", "Jonctiune-1226", "Jonctiune-1224", "SenzorChisinau-Titulescu", "248-B", "247-A", "248-A", "247-B", "Jonctiune-2755", "Jonctiune-3470", "751-B", "Jonctiune-2773", "286-B", "286-A", "249-A", "250-B", "249-B", "250-A", "PT3", "Jonctiune-J-31", "Jonctiune-J-20", "Jonctiune-4602", "Jonctiune-4618", "288-A", "288-B", "287-A", "287-B", "281-A", "Jonctiune-2199", "283-A", "283-B", "281-B", "282-B", "282-A", "Jonctiune-2200", "Jonctiune-1638", "PT4", "Jonctiune-2206", "Jonctiune-1646", "Jonctiune-4595", "Jonctiune-3464", "Jonctiune-3075", "Jonctiune-4614", "Jonctiune-1872", "Jonctiune-J-16", "Jonctiune-1637", "Jonctiune-2738", "231-A", "231-B", "Jonctiune-1636", "Jonctiune-2739", "Jonctiune-2207", "236-A", "236-B", "237-B", "237-A", "233-B", "233-A", "232-B", "232-A", "260-A", "260-B", "259-A", "259-B", "261-A", "261-B", "Jonctiune-1641", "Jonctiune-2201", "Jonctiune-2203", "230-B", "230-A", "Jonctiune-3068", "Jonctiune-J-34", "Jonctiune-2204", "Jonctiune-2205", "Jonctiune-1635", "258-A", "258-B", "Jonctiune-2736", "Jonctiune-1634", "229-B", "229-A", "Jonctiune-2737", "Jonctiune-1632", "PT1", "276-B", "276-A"], "1": ["Jonctiune-J-15", "J-1644", "Jonctiune-1642", "Jonctiune-2744", "SenzorComunarzi-castanului", "235-A", "235-B", "Jonctiune-2735", "228-A", "228-B", "226-A", "226-B", "Jonctiune-1628", "PT2", "Jonctiune-2879", "Jonctiune-1875", "241-A", "241-B", "SenzorComunarzi-NatVech", "Jonctiune-4619", "Jonctiune-1414", "268-A", "268-B", "270-B", "270-A", "269-A", "269-B", "207-A", "207-B", "271-B", "271-A", "Jonctiune-2186", "217-B", "217-A", "218-A", "218-B", "254-A", "254-B", "210-B", "210-A", "Jonctiune-1995", "Jonctiune-1877", "Jonctiune-2177", "Jonctiune-3972", "Jonctiune-1998", "Jonctiune-1997", "Jonctiune-1996", "Jonctiune-1616", "Jonctiune-2743", "Jonctiune-3913", "Jonctiune-1606", "Jonctiune-3912", "Jonctiune-3510", "Jonctiune-1874", "215-A", "215-B", "216-B", "216-A", "240-A", "240-B", "275-B", "275-A", "Jonctiune-3471", "Jonctiune-4743", "213-B", "213-A", "214-B", "214-A", "212-A", "212-B", "Jonctiune-2176", "Jonctiune-4731", "Jonctiune-2185", "205-A", "205-B", "Jonctiune-2182", "206-B", "206-A", "Jonctiune-2181", "Jonctiune-267", "Jonctiune-1873", "Jonctiune-12372", "Jonctiune-J-23", "Jonctiune-2191", "Jonctiune-1415", "Jonctiune-1610", "Jonctiune-1413", "265-B", "265-A", "267-B", "267-A", "266-B", "266-A", "264-B", "264-A", "198-A", "198-B", "Jonctiune-1404", "Jonctiune-2180", "Jonctiune-2179", "SenzorCernauti-Sebesului", "Jonctiune-2196", "Jonctiune-3967", "Jonctiune-1407", "Jonctiune-2190", "Jonctiune-4742", "Jonctiune-1405", "Jonctiune-2189", "200-A", "200-B", "201-A", "201-B", "199-B", "199-A", "253-A", "253-B", "Jonctiune-3921", "202-A", "202-B", "203-B", "203-A", "Jonctiune-1406", "Jonctiune-2188", "Jonctiune-2193", "Jonctiune-2192"], "2": ["Jonctiune-2187", "Jonctiune-1421", "Jonctiune-2777", "263-A", "263-B", "Jonctiune-3961", "Jonctiune-2195", "Jonctiune-3566", "Jonctiune-2194", "Jonctiune-2776", "Jonctiune-1419"], "3": ["Jonctiune-2184", "748-B", "Jonctiune-2968", "291-A", "291-B", "290-A", "290-B", "Jonctiune-3974", "Jonctiune-2967"]}}

for i in range(100):
    print(i)
    producer.send(topic, value=message)
    sleep(30)