from typing import Any, Dict
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

class PushToDB():

    def __init__(self, config:str='', token = "", url="http://localhost:8086", org="TestOrg" ):
        # config ne dele
        self.token = token
        self.url = url
        self.org = org
        
        self.client = InfluxDBClient(url=self.url, token=self.token, org=self.org)

    def write_data(self, to_write: Dict[str, Any], bucket: str,
                   measurement: str, timestamp: int, tags: dict={}):
        writer = self.client.write_api(write_options=SYNCHRONOUS)
        writer.write(bucket, self.org,
                     [{"measurement": measurement,
                     "tags": tags, "fields": to_write,
                     "time": timestamp}])

    def push_data(self, point, bucket: str = 'TestBucket'):
        writer = self.client.write_api(write_options=SYNCHRONOUS)
        writer.write(bucket=bucket, record=point)

    def create_point(self, measurement: str, time, tags: dict=None, fields:dict=None):
        point = Point(measurement)

        point.time(time)
        if tags != None:
            for key, value in tags.items():
                point = point.tag(key, value)
        if fields != None:
            for key, value in fields.items():
                point = point.field(key, value)
        
        return point
