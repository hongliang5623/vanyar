# -*- coding: utf-8 -*-

from utils import ListNode


head1 = ListNode(2)
n1 = ListNode(3)
n2 = ListNode(3)
n3 = ListNode(4)
n4 = ListNode(4)
n5 = ListNode(9)
head1.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print 'source------------->>'
source = head1
while source:
    print source.val
    source = source.next

print 'run   ------------->>'
def rotateRight(head, k):
    if head == None:
        return head
    dummy = ListNode(0)
    dummy.next = head
    p = dummy
    count = 0
    while p.next:
        p = p.next
        count += 1
    p.next = dummy.next  # 构成环装链表
    step = count - ( k % count )
    if k == 0 or step == 0:
        return head

    for i in range(0, step):
        print p.val
        p = p.next
    print 'head:%s, head.next:%s, p.next:%s, p.next.next:%s' % (
        head.val, head.next.val, p.next.val, p.next.next.val)

    head = p.next
    p.val = 100000
    p.next = None  # 从P处断开环
    return head


def rotateRight2(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """

    if not head:
        return None

    if not head.next:
        return head

    pointer = head
    count = 1
    while pointer.next:
        pointer = pointer.next
        count+=1

    rotateTimes = k%count

    print("count is ", count)
    print('rotate is', rotateTimes)
    if not k or not rotateTimes:
        return head


    slow = fast = head

    for i in range(rotateTimes-1):
        fast = fast.next

    tmp = ListNode(0)

    while fast.next:
        tmp = slow
        slow = slow.next
        fast = fast.next


    print 'tmp before slow:%s, fast:%s, slow:%s' % (tmp.val, fast.val, slow.val)
    tmp.next = None  # 断开旋转点之前的指针指向，保证slow为头部
    fast.next = head  # 末尾指向头部
    return slow


result = rotateRight2(head1, 2)
print 'result---------->>>>'
while result:
    print result.val
    result = result.next
