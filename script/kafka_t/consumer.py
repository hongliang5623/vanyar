# -*- coding: utf-8 -*-


from kafka import KafkaConsumer
import time

def log(str_):
        t = time.strftime(r"%Y-%m-%d_%H-%M-%S",time.localtime())
        print("[%s]%s"%(t,str_))

log('start consumer')
#消费192.168.120.11:9092上的world 这个Topic,指定consumer group是consumer-20171017
consumer=KafkaConsumer('world', group_id='consumer-20171017', bootstrap_servers=['192.168.120.11:9092'])
for msg in consumer:
        recv = "%s:%d:%d: key=%s value=%s" %(msg.topic,msg.partition,msg.offset,msg.key,msg.value)
        log(recv)

