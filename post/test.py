import time
from datetime import datetime

dt = "2020-12-29 00:00:00"
t = dt.split()

new = t[0] + "T" + t[1] + ".00Z"
print(new)

print(time.mktime(datetime.strptime(dt, "%Y-%m-%d %H:%M:%S").timetuple()))
a=str([1, 2, 3])
print(a)
"qatrYs6Aw5N8q_pXYxo0rk8bN6xOhTog-sTGVCcHaCxDi4SuS22Ruwiy0S1KLrbWuoeYTuepO_xYepmXk31tdA=="