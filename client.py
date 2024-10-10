from sense_hat import SenseHat
import random
import influxdb_client
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import time

sense = SenseHat()
sense.clear()

token = "token"
org = "org"
url = "url"
bucket = "bucket"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org).write_api(write_options=SYNCHRONOUS)

while True:
    point = Point("temps").tag("laite-id", 0).field("temp", sense.get_temperature())
    client.write(bucket=bucket, org=org, record=point)
    time.sleep(30)