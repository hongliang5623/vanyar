# -*- coding: utf-8 -*-

import random


def get_randata(num=10):
    datas = []
    while len(datas) < num:
        datas.append(random.randint(0,100))
    return datas


def quick_sort(ll):

    length = len(ll)
    if length <= 1:
        return ll

    base_index = random.randint(0, length-1)
    base = ll[base_index]
    right = []
    left = []

    for x in range(0, length):
        if ll[x] < base:
            left.append(ll[x])
        else:
            right.append(ll[x])

    return quick_sort(left) + quick_sort(right)

if __name__ == '__main__':
    datas = get_randata(14)
    print 'source....', datas
    result = quick_sort(datas)
    print 'result....', result
