# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None

class Huffman(object):

    def __init__(self, items=[]):
        while len(items)!=1:
            a, b = items[0], items[1]
            newvalue = a.value + b.value
            newnode = Node(value=newvalue)
            newnode.left, newnode.right = a, b
            items.remove(a)
            items.remove(b)
            items.append(newnode)
            items = sorted(items, key=lambda node: int(node.value))
            # 每次都要记得更新新的霍夫曼树的根节点
            self.root = newnode

    def print_huff(self):
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.value)
            if(current.left):
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print('---------------end----------------------')


if __name__ == '__main__':
    ls = [Node(i) for i in range(1, 6)]
    huffman = Huffman(items=ls)
    huffman.print_huff()

