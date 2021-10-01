import time
from datetime import datetime

dt = "2020-12-29 00:00:00"
t = dt.split()

new = t[0] + "T" + t[1] + ".00Z"
print(new)

print(time.mktime(datetime.strptime(dt, "%Y-%m-%d %H:%M:%S").timetuple()))
