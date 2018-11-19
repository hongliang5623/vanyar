# -*- coding: utf-8 -*-

"""
连续子数组的最大和
Content: 输入一个整形数组，有正数和负数，数组中的一个或连续多
个整数组成一个子数组，O(n)时间求所有子数组的和的最大值。
"""

def function(lists):
    max_sum = lists[0]
    pre_sum = 0
    for i in lists:
        if pre_sum < 0:
            pre_sum = i
        else:
            pre_sum += i
        if pre_sum > max_sum:
            max_sum = pre_sum
    return max_sum

def main():
    lists=[6, -3, 1, -2, 7, -15, 1, 2, 2]
    print function(lists)


if __name__ == "__main__":
    main()
