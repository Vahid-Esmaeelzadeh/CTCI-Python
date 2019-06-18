class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insertInOrder(self, d):
        if d <= self.data:
            if self.left is None:
                self.left = Node(d)
            else:
                self.left.insertInOrder(d)
        else:
            if self.right is None:
                self.right = Node(d)
            else:
                self.right.insertInOrder(d)


def countPathsWithSum(root: Node, targetSum: int) -> int:
    if not root:
        return 0

    # count paths starting from root
    pathsFromRoot = countPathsWithSumFromNode(root, targetSum, 0)

    pathsOnLeft = countPathsWithSum(root.left, targetSum)
    pathsOnRight = countPathsWithSum(root.right, targetSum)

    return pathsFromRoot + pathsOnLeft + pathsOnRight

def countPathsWithSumFromNode(n: Node, targetSum: int, currentSum: int) -> int:
    if not n:
        return 0

    currentSum += n.data
    totalPaths = 0

    if currentSum == targetSum:
        totalPaths += 1

    totalPaths += countPathsWithSumFromNode(n.left, targetSum, currentSum)
    totalPaths += countPathsWithSumFromNode(n.right, targetSum, currentSum)

    return totalPaths

root = Node(20)
root.insertInOrder(10)
root.insertInOrder(4)
root.insertInOrder(-10)
root.insertInOrder(16)
root.insertInOrder(-8)
root.insertInOrder(30)
root.insertInOrder(34)
root.insertInOrder(0)
root.insertInOrder(7)

print(countPathsWithSum(root, 16))
