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

            if not n.left and not n.right:
                return depth

            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
root.left.left = TreeNode(9)
root.right.left.left = TreeNode(11)
print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


