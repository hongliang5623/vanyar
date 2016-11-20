#!/usr/bin/python
#-*- encoding: utf-8 -*-
import os
import sys
import ConfigParser
import time
from lxml.html.soupparser import fromstring
from lxml.html import tostring
reload(sys)
sys.setdefaultencoding('utf8')


class ArkEbook(dict):

    kind = 1000
    kind_name = 'ebook'
    kind_name_cn = '电子书'

    def __getattr__(self, k):
        if k not in self:
            raise ValueError
        return self[k]

    def __setattr__(self, k, v):
        self[k] = v


if __name__ == '__main__':
    print '123'
    ebook = ArkEbook({'name': 'zhangsan'})
    print ebook.name
    print ebook.get('name')
    print ebook.get('age')

