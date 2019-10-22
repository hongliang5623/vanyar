# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def _reverse(self, start, end):

        pre_head = ListNode(0)
        pre_head.next = start
        current_head = pre_head.next

        print 'begin----------->, start:%s' % start.val
        while pre_head.next != end:
            print 'current head.next:%s' % current_head.next.val
            _next = current_head.next # 记录下一个节点 
            current_head.next = _next.next
            _next.next = pre_head.next
            pre_head.next = _next # 走到下一个节点
        print 'ok....'
        return [end, current_head]

    def reverse(self, start, end):
      pre, cur = None, None
      while start.next != end:
        next = start.next
        start.next = pre
        pre = start
        start = next
      return [end, pre]


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
    '''
    source = node1
    while source.next:
      print source.val
      source = source.next
    '''
    r = Solution().reverseKGroup(node1, 4)
    while r:
        print r.val
        r = r.next

