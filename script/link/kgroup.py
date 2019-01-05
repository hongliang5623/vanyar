# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverse(self, start, end):

        newhead = ListNode(0)
        newhead.next = start
        oldhead = newhead.next

        print 'begin----------->, start:%s' % start.val
        while newhead.next != end:
            print 'oldhead.next:%s' % oldhead.next.val
            tmp = oldhead.next
            oldhead.next = tmp.next
            tmp.next = newhead.next
            newhead.next = tmp
        print 'ok....'
        return [end, oldhead]

    def reverseKGroup(self, head, k):
        if head == None:
            return None

        nhead = ListNode(0)
        nhead.next = head
        start = nhead

        while start.next:
            end = start
            for i in range(k-1):
                end = end.next
                if end.next == None:
                    return nhead.next
            res=self.reverse(start.next, end.next)
            start.next = res[0]
            start=res[1]

        return nhead.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node11 = ListNode(11)
    node12 = ListNode(12)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)
    node10 = ListNode(10)
    node1.next = node11
    node11.next = node12
    node12.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node10
    r = Solution().reverseKGroup(node1, 4)
    while r:
        print r.val
        r = r.next

