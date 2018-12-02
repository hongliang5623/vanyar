# -*- coding: utf-8 -*-

import os

path = '/home/hongliang/workspace/vanyar'

for dirpath, dirname, filenames in os.walk(path):
    for file in filenames:
        fullpath = os.path.join(dirpath, file)
        print fullpath

lls = os.listdir(path)

for p in lls:
    n = '%s/%s' % (path, p)
    if not os.path.exists(n):
        continue
    print n
    if os.path.isdir(n):
        print os.listdir(n)
    else:
        print n

print '-------------------------------->>>>'
def getallfiles(dir):
    if not os.path.isdir(dir):
        print dir
        return

    dirlist = os.listdir(dir)
    for d in dirlist:
        full = '%s/%s' % (dir, d)
        if os.path.isdir(full):
            getallfiles(full)
        else:
            print full

getallfiles(path)
print 'end------------------------------>>>>'
