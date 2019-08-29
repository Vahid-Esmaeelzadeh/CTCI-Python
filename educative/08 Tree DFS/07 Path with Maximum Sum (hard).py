'''
Leaf to Leaf Path with Maximum Sum

Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.
A path can be defined as a sequence of nodes between any two leaf nodes and doesn’t necessarily pass through the root.
'''

import sys


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def find_maximum_path_sum(root):
    [_, max_path_sum] = helper(root)
    return max_path_sum


def helper(node):
    if node is None:
        return [0, -sys.maxsize]

    left_height_sum, left_leaf_to_leaf_max_sum = helper(node.left)
    right_height_sum, right_leaf_to_leaf_max_sum = helper(node.right)

    current_leaf_to_leaf_sum = left_height_sum + right_height_sum + node.val
    height_sum = max(left_height_sum, right_height_sum) + node.val

    max_leaf_to_leaf_sum = max(current_leaf_to_leaf_sum, left_leaf_to_leaf_max_sum, right_leaf_to_leaf_max_sum)

    return [height_sum, max_leaf_to_leaf_sum]


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))


main()
