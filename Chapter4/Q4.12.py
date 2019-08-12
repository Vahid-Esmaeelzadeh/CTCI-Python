'''
Paths with Sum: You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).
'''


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


# region brute force solution
def countPathsWithSum(root: Node, targetSum: int) -> int:
    if root is None:
        return 0

    # count paths starting from root
    pathsFromRoot = countPathsWithSumFromNode(root, targetSum, 0)

    pathsOnLeft = countPathsWithSum(root.left, targetSum)
    pathsOnRight = countPathsWithSum(root.right, targetSum)

    return pathsFromRoot + pathsOnLeft + pathsOnRight


def countPathsWithSumFromNode(n: Node, targetSum: int, currentSum: int) -> int:
    if n is None:
        return 0

    currentSum += n.data
    totalPaths = 0

    if currentSum == targetSum:
        totalPaths += 1

    totalPaths += countPathsWithSumFromNode(n.left, targetSum, currentSum)
    totalPaths += countPathsWithSumFromNode(n.right, targetSum, currentSum)

    return totalPaths
# endregion


# region optimal solution
def countPathsWithSum2(root: Node, targetSum: int) -> int:
    return countPathsWithSum_rcr(root, targetSum, 0, dict())


def countPathsWithSum_rcr(n: Node, targetSum: int, runningSum: int, pathCount: dict) -> int:
    if not n:
        return 0

    runningSum += n.data
    s = runningSum - targetSum

    # initial totalPaths 0 or the current value in the dictionary
    totalPaths = pathCount.get(s, 0)

    if runningSum == targetSum:
        totalPaths += 1

    pathCount[runningSum] = pathCount.get(runningSum, 0) + 1

    totalPaths += countPathsWithSum_rcr(n.left, targetSum, runningSum, pathCount)
    totalPaths += countPathsWithSum_rcr(n.right, targetSum, runningSum, pathCount)

    pathCount[runningSum] -= 1

    return totalPaths


def anySum(lst: list, targetSum: int) -> int:
    running_sum_count_dict = {}
    running_sum = 0
    total_count = 0

    for x in lst:
        running_sum += x
        running_sum_count_dict[running_sum] = running_sum_count_dict.get(running_sum, 0) + 1
        y = running_sum - targetSum
        total_count += running_sum_count_dict.get(y, 0)
        if y == 0:
            total_count += 1

    return total_count


# endregion

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

a = [10, 5, 1, 2, -1, -1, 7, 1, 2]
print(anySum(a, 15))