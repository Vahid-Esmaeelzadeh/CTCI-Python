class btreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrderPrint(n: btreeNode):
    if n is not None:
        print(n.data, end=' ')
        preOrderPrint(n.left)
        preOrderPrint(n.right)


def minHeight(a: list):
    return minHeight_helper(a, 0, len(a) - 1)

def minHeight_helper(a, start, end):

    if start > end:
        return None

    midIndex = (start + end) // 2
    n = btreeNode(a[midIndex])

    n.left = minHeight_helper(a, start, midIndex - 1)
    n.right = minHeight_helper(a, midIndex + 1, end)

    return n


a = [0, 5, 7, 9, 10, 12, 13, 17]
resultTree = minHeight(a)
preOrderPrint(resultTree)
print("\n")