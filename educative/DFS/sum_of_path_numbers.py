class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left, self.right = left, right


def find_sum_of_path_numbers(root):
    return find_sum_of_path_numbers_recursive(root, 0)


def find_sum_of_path_numbers_recursive(root, s):
    if root is None:
        return 0

    s = s * 10 + root.value

    if root.left is None and root.right is None:
        return s

    return find_sum_of_path_numbers_recursive(root.left, s) + find_sum_of_path_numbers_recursive(root.right, s)


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))
