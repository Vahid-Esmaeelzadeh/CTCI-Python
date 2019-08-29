'''
Second winner of tournament
'''

import math


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def second_winner(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return math.inf

    if root.val == root.left.val:  # we have to search left subtree
        return min(root.right.val, second_winner(root.left))

    return min(root.left.val, second_winner(root.right))


root = Node(1)
root.left = Node(1)
root.right = Node(3)
root.left.left = Node(1)
root.left.right = Node(2)
root.right.left = Node(3)
root.right.right = Node(4)

print(second_winner(root))
