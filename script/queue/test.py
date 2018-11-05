# -*- coding: utf-8 -*-

from Queue import Queue

q = Queue(maxsize=10)


if __name__ == '__main__':
    print 'begin....'

    for index in xrange(20):
        if not q.full():
            q.put(index)

    while q.qsize():
        print q.get()
