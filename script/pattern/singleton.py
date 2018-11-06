# -*- coding: utf-8 -*-

def singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)

print id(a1), a1.x
print id(a2), a2.x
a3 = A()
a3.x = 5
print a1.x

class Singleton(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance


s1 = Singleton.instance(a=2, b='dfd')
print id(s1), s1.args, s1.kwargs
s2 = Singleton.instance(a=22, c=33)
print id(s2), s2.args, s2.kwargs
