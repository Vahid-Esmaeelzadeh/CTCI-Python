'''
Connect All Level Order Siblings

Given a binary tree, connect each node with its level order successor.
The last node of each level should point to the first node of the next level.
'''

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect_all_siblings(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    previous = None
    while queue:
        current_node = queue.popleft()

        if previous:
            previous.next = current_node
        previous = current_node  # move previous pinter forward for next step

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()


main()
