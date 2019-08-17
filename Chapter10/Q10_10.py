'''
Rank from Stream: Imagine you are reading in a stream of integers. Periodically, you wish
to be able to look up the rank of a number x (the number of values less than or equal to x).
Implement the data structures and algorithms to support these operations. That is, implement
the method track(int x), which is called when each number is generated, and the method
getRankOfNumber(int x), which returns the number of values less than or equal to x(not
including x itself).

EXAMPLE

Stream(in order of appearance):5, 1, 4, 4, 5, 9, 7, 13, 3

getRankOfNumber(l) = 0
getRankOfNumber(3) = 1
getRankOfNumber(4) = 3

Tags: Creating a Binary Search Tree (BST)
'''
''' 
Pseudo Code
------------------------
getRank(node, x):
    if x == node.data:
        return node.leftSize
    if x is on left of node: 
        return getRank(node.left, x)
    if x is on right of node:
        return node.leftSize() + 1 + getRank(node.right, x)
------------------------------------------------------------        
'''


class RankNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.left_size = 0

    def insert(self, d):
        if d <= self.data:
            if self.left is not None:
                self.left.insert(d)
            else:
                self.left = RankNode(d)
            self.left_size += 1
        else:
            if self.right is not None:
                self.right.insert(d)
            else:
                self.right = RankNode(d)

    def get_rank(self, d):
        if d == self.data:
            return self.left_size
        elif d < self.data:
            if self.left is None:
                return -1
            else:
                return self.left.get_rank(d)
        else:
            if self.right is None:
                return -1
            else:
                return self.right.get_rank(d) + self.left_size + 1

    def track(self, num):
        if self.data is None:
            self.data = num
        else:
            self.insert(num)


root = RankNode()
root.track(5)
root.track(1)
root.track(4)
root.track(4)
root.track(5)
root.track(9)
root.track(7)
root.track(13)
root.track(3)

print(root.get_rank(7))


