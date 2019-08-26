'''
Random Node: You are implementing a binary search tree class from scratch, which, in addition
to insert, find, and delete, has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the methods.
'''

from random import *

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.size = 1

    def getRandomNode2(self):
        if self is None:
            return None
        i = randint(0, self.size - 1)
        return self.getIthNode(i)

    def getIthNode(self, i):
        leftSize = 0
        if self.left is not None:
            leftSize = self.left.size

        if i < leftSize:
            return self.left.getIthNode(i)
        elif i == leftSize:
            return self
        else:
            return self.right.getIthNode(i - (leftSize + 1))

    # def getRandomNode1(self):
    #     if self.left:
    #         leftSize = self.left.size
    #
    #     randIndex = randint(0, self.size - 1)
    #
    #     if randIndex < leftSize:
    #         return self.left.getRandomNode1()
    #     elif randIndex == leftSize:
    #         return self
    #     else:
    #         return self.right.getRandomNode1()

    def insertInOrder(self, d):
        if d <= self.data:
            if self.left is None:
                self.left = Node(d)
            else:
                self.left.insertInOrder(d)
        else:
            if self.right is None:
                self.right = Node(d)
            else:
                self.right.insertInOrder(d)
        self.size += 1

    def find(self, d):
        if d == self.data:
            return self
        elif d <= self.data:
            if self.left is None:
                return None
            else:
                return self.left.find(d)
        elif d > self.data:
            if self.right is None:
                return None
            else:
                return self.right.find(d)

        return None

root = Node(20)
root.insertInOrder(18)
root.insertInOrder(22)
root.insertInOrder(16)
root.insertInOrder(19)

for i in range(10):
    r1 = root.getRandomNode2()
    print(r1.data)

