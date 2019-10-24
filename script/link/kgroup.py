# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_link(source):
    if not source:
        return
    while source is not None:
        print source.val
        source = source.next
    print '<<<<<<<<<<<<<------------------>>>>>>>>>>>>>>>>>>'


class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def _reverse(self, start, end):

        new_head = ListNode(0)
        new_head.next = start    # 通过改变new_head.next直到end成为new_head.next
        new_end = new_head.next  # 通过改变new_end.next保留本此反转尾部

        while new_head.next != end:
            #:print 'new end: %s new end.next:%s ' % (new_end.val, new_end.next.val)
            cur = new_end.next  # 保存下一个节点
            new_end.next = cur.next
            cur.next = new_head.next
            new_head.next = cur  # 走到下一个节点

        new_head = end
        #print_link(new_head)
        #print_link(new_end)
        return new_head, new_end

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
            print 'recurse:start.next:%s, end.next:%s, nhead.next:%s' % (start.next.val, end.next.val, nhead.next.val)
            head_new, left_nodes =self._reverse(start.next, end.next)
            start.next = head_new  #这里仅修改一次nhead.next, start和nhead就不再指向同一内存了
            start=left_nodes

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
    #node9.next = node10
    source = node1
    print_link(source)
    print '--------->>begin........'
    r = Solution().reverseKGroup(node1, 4)
    while r:
        print r.val
        r = r.next

