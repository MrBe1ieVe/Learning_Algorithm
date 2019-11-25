# -*- coding: utf-8 -*-
'''
Python 3.x
Mr.BelieVe Created on 2019年11月23日
描述：链表
@author: Mr.BelieVe
@link: mrbelieve128.github.io
'''
class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Linkedlist(object):
    def __init__(self):
        self.head = Node()
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head.next = node
            self.length += 1
        else:
            curnode = self.head.next
            while curnode.next != None:
                curnode = curnode.next
            curnode.next = node
            self.length += 1

    def find(self, value):
        if self.length == 0:
            print("链表无内容")
            return None
        else:
            curnode = self.head.next
            _ = 0
            while curnode != None:
                if curnode.value == value:
                    _ += 1
                    print("在第{}个".format(_))
                    return _
                _ += 1
                curnode = curnode.next
            print("无此数值")
            return None

    def insert(self, value, place):


def main():
    L = Linkedlist()
    L.append(3)
    L.append(5)
    # L.append(7)
    print("链表长度", len(L))
    L.find(5)


if __name__ == '__main__':
    main()
