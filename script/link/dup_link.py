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

def deleteDuplicates():
    head = head1
    if head == None or head.next == None:
        return head
    dummy = ListNode(0)
    new = ListNode(0)
    dummy.next = head
    p = dummy
    while p.next:
        if p.next.next and p.next.val == p.next.next.val:
            p.next = p.next.next
        else:
            if new.next:
                temp = new.next
            else:
                temp = new
            temp.next = ListNode(p.next.val)
        p = p.next
    return new.next

def deleteDuplicates1():
    head = head1
    if head == None or head.next == None:
        return head
    p = head
    while p.next:
        if p.val == p.next.val:
            p.next = p.next.next
        else:
            p = p.next
    return head


result = deleteDuplicates()
print 'result---------->>>>'
while result:
    print result.val
    result = result.next
