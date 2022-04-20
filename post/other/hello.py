import re

sensor_name = re.findall("anomalies_braila_(.+)", "anomalies_braila_pressure_5772")[0]

print(sensor_name)