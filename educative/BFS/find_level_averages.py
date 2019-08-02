from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            n = queue.popleft()
            level_sum += n.value

            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)

        result.append(level_sum / level_size)

    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(find_level_averages(root))