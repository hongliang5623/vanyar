# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_link(source, info=''):
    if not source:
        return
    if info:
        print '---------------->>>:::', info
    while source is not None:
        print source.val
        source = source.next



def get_link_list():
    node1 = ListNode(1)
    cur = node1
    for item in [11, 12, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        dummy = ListNode(item)
        cur.next = dummy
        cur = dummy
    source = node1
    # node1.next = node2
    '''
    while source.next:
        print source.val
        source = source.next
    while node1.next:
        print node1.val
        node1 = node1.next
    '''
    return source


def reverse_link(source):
    if source is None or source.next is None:
        return source

    pre, new_head = None, source

    while new_head is not None:
        dummy = new_head.next
        new_head.next = pre
        pre = new_head
        new_head = dummy
        print 'dummy:%s, pre:%s, new_head:%s' % (
            dummy.val if dummy else 'null', pre.val, new_head.val if new_head else 'null')

    return pre


def reverse_link_to(source, end):
    if source is None or source.next is None:
        return source

    pre, new_head = None, source

    while new_head is not None:
        dummy = new_head.next
        new_head.next = pre
        pre = new_head
        new_head = dummy
        print 'dummy:%s, pre:%s, new_head:%s' % (
            dummy.val if dummy else 'null', pre.val, new_head.val if new_head else 'null')


if __name__ == '__main__':
    source = get_link_list()
    print_link(source, 'init....')
    after_reversed = reverse_link(source)
    print_link(after_reversed, 'reversed')
