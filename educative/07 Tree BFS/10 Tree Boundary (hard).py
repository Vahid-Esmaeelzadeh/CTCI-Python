'''
Tree Boundary

Given a binary tree, return an array containing all the boundary nodes of the tree in an anti-clockwise direction.

The boundary of a tree contains all nodes in the left view, all leaves, and all nodes in the right view.
Please note that there should not be any duplicate nodes. For example, the root is only included in the left view;
similarly, if a level has only one node we should include it in the left view.
'''

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_tree_boundary(root):
    if root is None:
        return []

    left_view = []
    right_view = deque()  # I have to save the right view in reverse order

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)

        for i in range(level_size):

            current_node = queue.popleft()

            if i == 0:  # first node
                left_view.append(current_node)
            elif i == level_size - 1:  # last node
                right_view.appendleft(current_node)

            #  add the children in the queue
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    leafs = []
    find_leaf_nodes(root, leafs)

    return left_view + leafs[1: len(leafs)-1] + list(right_view)


def find_leaf_nodes(root, leafs):
    if root is None:
        return
    if root.left is None and root.right is None:  # leaf node
        leafs.append(root)
        return

    find_leaf_nodes(root.left, leafs)
    find_leaf_nodes(root.right, leafs)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(9)
    root.left.right = TreeNode(3)
    root.left.right.left = TreeNode(15)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(6)
    root.right.right.left.left = TreeNode(8)
    root.right.right.left.right = TreeNode(2)
    result = find_tree_boundary(root)
    print("Tree boundary: ", end='')
    for node in result:
        print(str(node.val) + " ", end='')


main()
