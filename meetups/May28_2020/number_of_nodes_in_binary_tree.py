import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def num_of_nodes(root):
    if root is None:
        return 0

    return 1 + num_of_nodes(root.left) + num_of_nodes(root.right)


def num_of_full_nodes(root):
    if root is None:
        return 0

    c1 = num_of_full_nodes(root.left)
    c2 = num_of_full_nodes(root.right)

    is_root_full_node = (root.left is not None) and (root.right is not None)

    return int(is_root_full_node) + c1 + c2


def num_of_good_nodes(root):
    return helper(root, -math.inf)


def helper(root, maxNum):
    if root is None:
        return 0

    nextMaxNum = max(root.val, maxNum)
    return int(root.val >= maxNum) + helper(root.left, nextMaxNum) + helper(root.right, nextMaxNum)




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
root.right.left = TreeNode(5)

print(num_of_good_nodes(root))