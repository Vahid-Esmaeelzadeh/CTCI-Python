'''
all in one

I want to find the following items:
    1) all root-to-leaf paths
    2) all root-to-leaf paths with a given sum
    3) the root-to-leaf path with maximum sum
    4) the root-to-leaf path with minimum sum
'''

import sys


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def all_in_one(root, target_sum):
    # global objects
    all_paths = []
    all_target_paths = []
    max_sum_path = []
    max_sum = [0]            # I define it as a list to make it global
    min_sum_path = []
    min_sum = [sys.maxsize]  # I define it as a list to make it global

    # local objects
    current_path = []  # I have to undo operations on this to remove the effect of any change inside of function
    current_sum = 0

    helper(root, current_sum, current_path, target_sum, max_sum, max_sum_path, min_sum, min_sum_path,
           all_target_paths, all_paths)
    return [all_paths, all_target_paths, max_sum_path, max_sum, min_sum_path, min_sum]


def helper(current_node, current_sum, current_path, target_sum, max_sum, max_sum_path,
           min_sum, min_sum_path, all_target_paths, all_paths):
    if current_node is None:
        return

    current_sum += current_node.val
    current_path.append(current_node.val)

    if current_node.left is None and current_node.right is None:

        all_paths.append(list(current_path))  # 1   I have to write list(.)

        if current_sum == target_sum:   # 2
            all_target_paths.append(list(current_path))

        if current_sum > max_sum[0]:  # 3
            max_sum[0] = current_sum
            max_sum_path[:] = current_path
            # I have to write arr[:], simple assignment is not copying, arr = list(a) is not copying

        if current_sum < min_sum[0]:  # 4
            min_sum[0] = current_sum
            min_sum_path[:] = current_path
    else:
        helper(current_node.left, current_sum, current_path, target_sum,
               max_sum, max_sum_path, min_sum, min_sum_path, all_target_paths, all_paths)
        helper(current_node.right, current_sum, current_path, target_sum,
               max_sum, max_sum_path, min_sum, min_sum_path, all_target_paths, all_paths)

    del current_path[-1]


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.left.right = TreeNode(-1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(5)

    results = all_in_one(root, 18)
    print("All paths: " + str(results[0]))
    print("All target paths: " + str(results[1]))
    print("The path with max sum: " + str(results[2]))
    print("Max sum: " + str(results[3]))
    print("The path with min sum: " + str(results[4]))
    print("Min sum: " + str(results[5]))


main()
