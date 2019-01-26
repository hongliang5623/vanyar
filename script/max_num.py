# -*- coding: utf-8 -*-

def max_plus(nums):
    max_num = 0
    pre_max = 0
    for i in nums:
        if pre_max < 0:
            pre_max = i
        else:
            pre_max +=i
        max_num = max(pre_max, max_num)
    return max_num

if __name__ == '__main__':
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = max_plus(array)
    print res
