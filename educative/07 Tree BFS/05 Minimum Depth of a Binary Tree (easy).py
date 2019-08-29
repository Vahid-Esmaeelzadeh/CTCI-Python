'''
Minimum Depth of a Binary Tree

Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path
from the root node to the nearest leaf node.
'''

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None


def find_minimum_depth(root):
    if root is None:
        return 0

    depth = 0
    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        depth += 1

        for _ in range(level_size):
            n = queue.popleft()

            if not n.left and not n.right:  # this is the first leaf node
                return depth

            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)


# Maximum Depth of a Binary Tree
def find_maximum_depth(root):
    if root is None:
        return 0

    queue = deque()
    queue.append(root)
    maximumTreeDepth = 0
    while queue:
        maximumTreeDepth += 1
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()

            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

    return maximumTreeDepth


def minDepth_recursive(root):
    # Corner Case.Should never be hit unless the code is
    # called on root = NULL
    if root is None:
        return 0

    # Base Case : Leaf node.This acoounts for height = 1
    if root.left is None and root.right is None:
        return 1

    # If left subtree is Null, recur for right subtree
    if root.left is None:
        return minDepth_recursive(root.right) + 1

    # If right subtree is Null , recur for left subtree
    if root.right is None:
        return minDepth_recursive(root.left) + 1

    return min(minDepth_recursive(root.left), minDepth_recursive(root.right)) + 1


def maxDepth_recursive(root):
    if root is None:
        return 0

    h1 = maxDepth_recursive(root.left)
    h2 = maxDepth_recursive(root.right)

    return 1 + max(h1, h2)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
print("Tree Maximum Depth: " + str(find_maximum_depth(root)))
root.left.left = TreeNode(9)
root.right.left.left = TreeNode(11)
print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
print("Tree Maximum Depth: " + str(find_maximum_depth(root)))

print(minDepth_recursive(root))
print(maxDepth_recursive(root))