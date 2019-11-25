# -*- coding: utf-8 -*-
'''
Python 3.x
Mr.BelieVe Created on 2019年11月23日
描述：遍历二叉树
@author: Mr.BelieVe
@link: mrbelieve128.github.io
'''
class BiNode:
    def __init__(self, data=None, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BiTree:   
    def __init__(self):
        self.node = BiNode()
        self.root = self.Create()

    def Create(self):
        print("Input node data:")
        data = input()
        if data == '#':
            #self.node = None
            return self.node
        else:
            self.node = BiNode()
            self.node.data = data
            print("Current node {}. Please input left child".format(data))
            self.node.lchild = BiTree()
            print("Current node {}. Please input right child".format(data))
            self.node.rchild = BiTree()
        return self.node

    def PreOrder(self):
        if self.node.data == '#':
            return ''
        else:
            print(self.node.data, end='')
            _ = self.node.lchild
            if not _.node.data == None:
                # print("leftchild")
                print(_.PreOrder(), end='')
            _ = self.node.rchild
            if not _.node.data == None:
                # print("rightchild")
                print(_.PreOrder(), end='')
            return ''

    def InOrder(self):
        if self.node.data == '#':
            return ''
        else:
            _ = self.node.lchild
            if not _.node.data == None:
                # print("leftchild")
                print(_.PreOrder(), end='')
            print(self.node.data, end='')
            _ = self.node.rchild
            if not _.node.data == None:
                # print("rightchild")
                print(_.PreOrder(), end='')
            return ''
    def PostOrder(self):
        if self.node.data == '#':
            return ''
        else:
            _ = self.node.lchild
            if not _.node.data == None:
                # print("leftchild")
                print(_.PreOrder(), end='')
            _ = self.node.rchild
            if not _.node.data == None:
                # print("rightchild")
                print(_.PreOrder(), end='')
            print(self.node.data, end='')
            return ''


def main():
    BiTree_ = BiTree()
    RootNode = BiNode()
    print("-" * 10 + "前序排列" + "-" * 10)
    BiTree_.PreOrder()
    print()
    print("-" * 10 + "中序排列" + "-" * 10)
    BiTree_.InOrder()
    print()
    print("-" * 10 + "后序排列" + "-" * 10)
    BiTree_.PostOrder()



if __name__ == "__main__":
    main()
