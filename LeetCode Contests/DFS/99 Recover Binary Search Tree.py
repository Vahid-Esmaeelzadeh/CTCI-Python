'''
99. Recover Binary Search Tree
'''

import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def recoverTree(root):
    nodes = []
    inorder(root, nodes)
    print(nodes[0].val, nodes[1].val)


def inorder(root, nodes):
    if root is None:
        return

    inorder(root.left, nodes)

    if len(nodes) == 0:
        nodes.append(root)
    if len(nodes) == 1:
        if root.val >= nodes[0].val:
            nodes[0] = root
        else:
            nodes.append(root)
    if len(nodes) == 2 and root.val < nodes[1].val:
            nodes[1] = root

    inorder(root.right, nodes)


def inorder_traverse(root):
    if root is None:
        return

    inorder_traverse(root.left)
    print(root.val, end=" ")
    inorder_traverse(root.right)


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)


recoverTree(root)