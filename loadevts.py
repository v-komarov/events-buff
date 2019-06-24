#!/usr/bin/python3.6
import datetime
import json
from cassandra.cluster import Cluster
from kafka import KafkaConsumer,TopicPartition


import conf

cluster = Cluster(conf.ca_host,conf.ca_port)
session = cluster.connect()
session.set_keyspace(conf.ca_keyspace)

consumer = KafkaConsumer(conf.ka_queue,bootstrap_servers=conf.ka_host, auto_offset_reset='latest')

for m in consumer:

    j = m.value.decode()
    #print(j)
    evid = json.loads(j)["evid"]

    session.execute("""INSERT INTO events.events_buff (evt_id,datetime_evt,data) VALUES(%s,%s,%s) USING TTL 1200;""", (evid,datetime.datetime.now(),j))
