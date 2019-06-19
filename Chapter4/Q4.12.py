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

def countPathsWithSum2(root: Node, targetSum: int) -> int:
    return countPathsWithSum_rcr(root, targetSum, 0, dict())
def countPathsWithSum_rcr(n: Node, targetSum: int, runningSum: int, pathCount: dict) -> int:
    if not n:
        return 0

    runningSum += n.data
    s = runningSum - targetSum
    totalPaths = 0

    if s in pathCount:
        totalPaths = pathCount[s]

    if runningSum == targetSum:
        totalPaths += 1

    if runningSum in pathCount:
        pathCount[runningSum] += 1
    else:
        pathCount[runningSum] = 1

    totalPaths += countPathsWithSum_rcr(n.left, targetSum, runningSum, pathCount)
    totalPaths += countPathsWithSum_rcr(n.right, targetSum, runningSum, pathCount)

    pathCount[runningSum] -= 1

    return totalPaths

def anySum(lst: list, targetSum: int) -> int:
    # I should implement
    return 0

def nSum(lst: list, targetSum: int, n: int) -> int:
    # generalized version of two-sum, three-sum problems
    return 0

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
print(countPathsWithSum2(root, 16))

