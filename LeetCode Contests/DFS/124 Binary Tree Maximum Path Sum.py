'''
124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along
the parent-child connections. The path must contain at least one node and does not need to go through the root.
'''
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        [maxSum, _] = self.maxSumRecursive(root)
        return maxSum

    def maxSumRecursive(self, root: TreeNode) -> [int, int]:
        if root is None:
            return [-math.inf, -math.inf]

        maxSum_left, maxSum_from_root_left = self.maxSumRecursive(root.left)
        maxSum_right, maxSum_from_root_right = self.maxSumRecursive(root.right)

        maxSum = max(maxSum_left, maxSum_right, root.val + maxSum_from_root_left, root.val + maxSum_from_root_right,
                   root.val + maxSum_from_root_left + maxSum_from_root_right, root.val)
        maxSum_from_root = max(root.val + maxSum_from_root_left, root.val + maxSum_from_root_right, root.val)

        return [maxSum, maxSum_from_root]


root = TreeNode(2)
root.left = TreeNode(-1)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

sol = Solution()
print(sol.maxPathSum(root))