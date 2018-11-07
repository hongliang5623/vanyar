# coding: utf-8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def nonrecurse(head):  # 循环的方法反转链表
    if head is None or head.next is None:
        return head
    pre, new_head = None, None
    cur = head
    while cur:
        new_head = cur
        cur_next = cur.next
        cur.next = pre
        pre = cur
        cur = cur_next
    return new_head


def recurse(head, newhead):  # 递归，head为原链表的头结点，newhead为反转后链表的头结点
    if head is None:
        return
    if head.next is None:
        newhead = head
    else:
        newhead = recurse(head.next, newhead)
        head.next.next = head # 当前节点的next节点指向自己
        head.next = None # 当前节点原来的指向制空
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
    source_head1 = init_link(20)
    print_link(source_head1, 'source')

    p1 = nonrecurse(source_head1)
    print_link(p1, 'non---->')

    source_head2 = init_link(20)
    print_link(source_head2, 'source2')
    p2 = recurse(source_head2, None)
    print_link(p2, 'recurse---->')
