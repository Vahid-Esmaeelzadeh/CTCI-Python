'''
1110. Delete Nodes And Return Forest
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def delNodes(self, root: TreeNode, to_delete):
        roots = [root]
        self.delNodes_helper(root, set(to_delete), roots)
        return roots

    def delNodes_helper(self, root, to_delete, roots):
        if root is None:
            return []

        if root.val in to_delete:
            if root in roots:
                roots.remove(root)

            if root.left:
                roots.append(root.left)
            if root.right:
                roots.append(root.right)

        l = root.left
        r = root.right

        if root.left and root.left.val in to_delete:
            root.left = None
        if root.right and root.right.val in to_delete:
            root.right = None

        self.delNodes_helper(l, to_delete, roots)
        self.delNodes_helper(r, to_delete, roots)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
to_delete = [3, 5]

sol = Solution()
print(sol.delNodes(root, to_delete))

