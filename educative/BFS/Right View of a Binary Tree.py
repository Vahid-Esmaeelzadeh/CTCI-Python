'''
Right View of a Binary Tree

Given a binary tree, return an array containing nodes in its right view.
The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
'''

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def tree_right_view(root):
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            current_node = queue.popleft()

            # if it is the last node of this level, add it to the result
            if i == level_size - 1:  # append the last node in the current level
                result.append(current_node)

            # insert the children of current node in the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')


main()
