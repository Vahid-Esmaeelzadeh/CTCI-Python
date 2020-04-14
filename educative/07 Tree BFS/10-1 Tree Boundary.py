from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_tree_boundary(root):
    if root is None:
        return []

    leftView, rightView = [], deque()

    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        for i in range(levelSize):
            currentNode = queue.popleft()

            if currentNode.left is None and currentNode.right is None:  # skip leaf nodes
                # We need to skip leaf nodes to avoid repetitive nodes in leftview/rightview and leaves
                continue
            elif i == 0:  # if it is the first node of this level, add it to the leftView
                leftView.append(currentNode.val)
            elif i == levelSize - 1:  # if it is the last node of this level, add it to the rightView
                # because of bottom-up direction, we need to generate the rightView in the reverse direction
                rightView.appendleft(currentNode.val)

            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

    return leftView + find_leaves_dfs(root) + list(rightView)


def find_leaves_dfs(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.val]

    return find_leaves_dfs(root.left) + find_leaves_dfs(root.right)

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
    result = find_tree_boundary(root)
    print("Tree boundary: ", end='')
    for node in result:
        print(str(node) + " ", end='')


main()
