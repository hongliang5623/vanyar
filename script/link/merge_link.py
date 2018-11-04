# -*- coding: utf-8 -*-

from utils import ListNode


def merge_two_list(link1, link2):
    new_head = ListNode(0)
    pre = new_head
    while link1 and link2:
        if link1.val < link2.val:
            pre.next = link1
            link1 = link1.next
        else:
            pre.next = link2
            link2 = link2.next
        pre = pre.next

    if link1:
        pre.next = link1

    if link2:
        pre.next = link2

    return new_head.next


head1 = ListNode(2)
n1 = ListNode(3)
n2 = ListNode(4)
n3 = ListNode(9)
head1.next = n1
n1.next = n2
n2.next = n3

head2 = ListNode(3)
m1 = ListNode(5)
m2 = ListNode(7)
m3 = ListNode(8)
head2.next = m1
m1.next = m2
m2.next = m3
res = merge_two_list(head1, head2)

while res:
    print res.val
    res = res.next
