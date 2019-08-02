from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None


def zigzag_traverse(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    left_to_right = True

    while queue:
        level_size = len(queue)
        current_level = deque()

        for _ in range(level_size):
            n = queue.popleft()

            if left_to_right:
                current_level.append(n.value)
            else:
                current_level.appendleft(n.value)

            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)

        result.append(current_level)
        left_to_right = not left_to_right

    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(zigzag_traverse(root))
