# -*- coding: utf-8 -*-

import Queue

index_q = Queue.Queue()

for index in xrange(10):
    index_q.put(index)

while not index_q.empty():
    print index_q.get()
