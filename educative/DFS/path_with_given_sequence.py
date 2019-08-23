'''
Path With Given Sequence

Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
'''


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left, self.right = left, right


def has_path_with_given_sequence(root, seq):
    if root is None or len(seq) == 0:
        return False

    if root.value != seq[0]:
        return False

    if root.left is None and root.right is None and len(seq) == 1 and root.value == seq[0]:
        return True

    return has_path_with_given_sequence(root.left, seq[1:]) or has_path_with_given_sequence(root.right, seq[1:])


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)

print("Tree has path sequence: " + str(has_path_with_given_sequence(root, [1, 0, 7])))
print("Tree has path sequence: " + str(has_path_with_given_sequence(root, [1, 1, 6])))
