class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left, self.right = left, right


def dfs_print(root):
    if root is None:
        return
    print(root.value, end=" ")
    dfs_print(root.left)
    dfs_print(root.right)


def has_path_with_sum(root, s):
    if root is None:
        return False

    if root.value == s and root.left is None and root.right is None:
        return True

    return has_path_with_sum(root.left, s - root.value) or has_path_with_sum(root.right, s - root.value)

    # if root is None and s == 0:
    #     return True
    #
    # if root:
    #     return has_path_with_sum(root.left, s - root.value) or has_path_with_sum(root.right, s - root.value)
    #
    # return False


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Tree has path: " + str(has_path_with_sum(root, 23)))
print("Tree has path: " + str(has_path_with_sum(root, 16)))

dfs_print(root)
print()
