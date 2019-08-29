'''
Tree BFS - Level Order Traversal

Given a binary tree, populate an array to represent its level-by-level traversal.
You should populate the values of all nodes of each level from left to right in separate sub-arrays.

it should return a list of lists
'''

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None


def print_bfs_traverse(root):
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        n = queue.popleft()
        print(n.value, end=" ")
        if n.left:
            queue.append(n.left)
        if n.right:
            queue.append(n.right)
    print()


# Level Order Traversal
def traverse(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            n = queue.popleft()
            current_level.append(n.value)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)

        result.append(current_level)

    return result


# Reverse Level Order Traversal
def traverse_inverse(root):
    result = deque()
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            n = queue.popleft()
            current_level.append(n.value)
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)

        result.appendleft(current_level)

    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print_bfs_traverse(root)

print(traverse(root))
print(traverse_inverse(root))
