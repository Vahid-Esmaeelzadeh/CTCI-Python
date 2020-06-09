# 1457. Pseudo-Palindromic Paths in a Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pseudoPalindromicPaths(root: TreeNode) -> int:
    nodes = set()
    return helper(root, nodes)


def helper(root, nodes):
    if root is None:
        return 0

    if root.val not in nodes:
        nodes.add(root.val)
    else:
        nodes.remove(root.val)

    if root.left is None and root.right is None:
        res = int(len(nodes) <= 1)
        if root.val not in nodes:
            nodes.add(root.val)
        else:
            nodes.remove(root.val)
        return res

    count = helper(root.left, nodes) + helper(root.right, nodes)

    if root.val not in nodes:
        nodes.add(root.val)
    else:
        nodes.remove(root.val)

    return count


def pseudoPalindromicPaths_bit(root: TreeNode) -> int:
    return helper_bit(root, 0)


def helper_bit(root, count):
    if root is None:
        return 0

    count ^= pow(2, root.val)

    if root.left is None and root.right is None:
        return int(count == 0 or (count & count-1) == 0)

    return helper_bit(root.left, count) + helper_bit(root.right, count)


root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.right = TreeNode(1)

print(pseudoPalindromicPaths_bit(root))
