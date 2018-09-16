from collections import OrderedDict

nums = [2, -3, 2, -3, -2, 4]


def max_product(nums):

    min_curr, max_curr, max_total = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        n = nums[i]
        min_curr, max_curr = n * min(1, min_curr), n * max(1, max_curr)
        if n < 0:
            min_curr, max_curr = max_curr, min_curr

        max_total = max(max_total, max_curr)

    return max_total


def lengthOfLongestSubstring(source):
    start = 0
    maxlen = 0
    dict = OrderedDict({})
    source_length = len(source)
    max_strs = []

    for i in range(source_length):
        dict[source[i]] = -1

    for i in range(source_length):
        str_now = source[i]

        if dict[str_now] != -1:
            while start <= dict[str_now]:
                dict[source[start]] = -1
                start += 1

        if i + 1 - start > maxlen:
            maxlen = i + 1 - start
        if i + 1 - start >= maxlen:
            max_str = source[start:start + maxlen]
            max_strs.append(max_str)
            max_strs = filter(lambda s: len(s) >= maxlen, max_strs)

        dict[str_now] = i
        print str_now, max_strs
    return maxlen


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse(start, end):
    newhead = ListNode(0)
    newhead.next = start
    while newhead.next != end:
        tmp = start.next
        start.next = tmp.next
        tmp.next = newhead.next
        newhead.next = tmp
    return [end, start]


def reverseKGroup(head, k):
    if head == None:
        return None
    nhead = ListNode(0)
    nhead.next = head
    start = nhead
    while start.next:
        end = start
        for i in range(k - 1):
            end = end.next
            if end.next == None:
                return nhead.next
        res = reverse(start.next, end.next)
        start.next = res[0]
        start = res[1]
    return nhead.next


if __name__ == '__main__':
    # print max_product(nums=nums)
    print lengthOfLongestSubstring('abcaaadfb')
