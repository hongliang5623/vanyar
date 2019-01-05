# -*- coding: utf-8 -*-

from utils import ListNode


head1 = ListNode(2)
n11 = ListNode(2)
n12 = ListNode(5)
n1 = ListNode(3)
n2 = ListNode(3)
n3 = ListNode(4)
n4 = ListNode(4)
n5 = ListNode(9)
head1.next = n11
n11.next = n12
n12.next = n2
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

source = head1
print 'source data------>>'
while source:
    print source.val
    source = source.next

def deleteDuplicates():
    head = head1
    if head == None or head.next == None:
        return head
    dummy = ListNode(0)
    dummy.next = head
    p = dummy
    tmp = dummy.next

    while p.next:
        print 'p:%s,p.next:%s -----, tmp:%s' % (p.val, p.next.val, tmp.val)
        while tmp.next and tmp.next.val == p.next.val:
            tmp = tmp.next
        print '------>temp:', tmp.val
        if tmp == p.next:
            print 'tmp=====p.next'
            p = p.next
            tmp = p.next
        else:
            print 'tmp:%s!!!!!!=====p.next:%s' % (tmp.val, p.next.val)
            p.next = tmp.next

    return dummy.next


def deleteDuplicates2():
    head = head1
    if head == None or head.next == None:
        return head

    new = ListNode(0)
    dummy = ListNode(0)
    dummy.next = head
    p = dummy

    while p.next:
        print '------>>', p.val
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
