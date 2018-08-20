# coding: utf-8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def nonrecurse(head):  # 循环的方法反转链表
    if head is None or head.next is None:
        return head
    pre = None
    cur = head
    h = head
    while cur:
        h = cur
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return h


def recurse(head, newhead):    #递归，head为原链表的头结点，newhead为反转后链表的头结点
    if head is None:
        return
    if head.next is None:
        newhead = head
    else:
        newhead = recurse(head.next, newhead)
        head.next.next = head
        head.next = None
    return newhead


def init_link(length=10):
    node_list = [ListNode(i) for i in xrange(length)]
    head = node_list[0]
    dummy = None
    for index in xrange(len(node_list) - 1):
        if index == 0:
            dummy = head
        dummy.next = node_list[index + 1]
        dummy = dummy.next
    return head


def print_link(p, flag=''):
    while p:
        print flag, p.val
        p = p.next


if __name__ == '__main__':
    source_head = init_link(20)
    print_link(source_head, 'source')

    p1 = nonrecurse(source_head)
    print_link(p1, 'non')

    p2 = recurse(init_link(20), None)
    print_link(p2, 'recurse')
