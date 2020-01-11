'''
572. Subtree of Another Tree
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None:
            return False

        res = False
        if s.val == t.val:
            res = self.isEqualTrees(s, t)

        return res or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


    def isEqualTrees(self, s, t):
        if s is None and t is None:
            return True
        if s and t is None:
            return False
        if t and s is None:
            return False
        if s.val != t.val:
            return False

        return self.isEqualTrees(s.left, t.left) and self.isEqualTrees(s.right, t.right)

sol = Solution()
s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)

t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)

print(sol.isSubtree(s, t))
