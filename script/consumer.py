# -*- coding: utf-8 -*-

import threading
import time
import Queue


q = Queue.Queue(maxsize=10)


def producer(name):  #生产者
    count = 1
    while count < 100:
        q.put("馒头%s" % count)
        print"生产了馒头", count
        count += 1
        time.sleep(0.5)
    print '今天馒头已经售罄。。。。。。。。：'


def consumer(name):  #消费者
    count = 0
    while count < 100:
        count +=1
        print "[%s]取到[%s]并且吃了它..." % (name, q.get())
        print '现有馒头数量：%s' % q.qsize()
        time.sleep(1)


p = threading.Thread(target=producer, args=("Tim",))
c1 = threading.Thread(target=consumer, args=("King",))
c2 = threading.Thread(target=consumer, args=("Wang",))

p.start()
c1.start()
c2.start()

p.join()
c1.join()
c2.join()
