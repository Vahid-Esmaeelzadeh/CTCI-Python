'''
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
'''

from Common.common import *


class BtreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# region Using list of regular lists
def listsOfDepths(n: BtreeNode):
    lst = []
    depth_helper(n, lst, 0)
    return lst


def depth_helper(n: BtreeNode, lst, level):
    if n is None:
        return

    if len(lst) == level:  # this is the first time that we are in this level  => we should append a list for this level
        lst.append([n.data])
    else:  # we already have a list for this level
        lst[level].append(n.data)

    depth_helper(n.left, lst, level + 1)
    depth_helper(n.right, lst, level + 1)
# endregion
# region Using list of LinkedLists
def LLsOfDepths(n: BtreeNode):
    lst = []
    depth_helper(n, lst, 0)
    return lst


def LLs_depth_helper(n: BtreeNode, lst, level):
    if n is None:
        return

    if len(lst) == level:  # this is the first time that we are in this level  => we should append a list for this level
        lst.append(linkedList(n.data))
    else:  # we already have a list for this level
        lst[level].addLast(n.data)

    depth_helper(n.left, lst, level + 1)
    depth_helper(n.right, lst, level + 1)

# endregion

root = BtreeNode(10)
root.left = BtreeNode(20)
root.right = BtreeNode(15)
root.left.left = BtreeNode(3)
root.left.right = BtreeNode(0)
root.right.left = BtreeNode(100)
root.right.right = BtreeNode(-99)

nodesList = listsOfDepths(root)
print(nodesList)

LL_nodesList = LLsOfDepths(root)
for n in LL_nodesList:
    print(n)


