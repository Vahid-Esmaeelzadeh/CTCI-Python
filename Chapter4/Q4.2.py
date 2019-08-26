'''
Minimal Height Tree: Given a sorted (increasing order) array with unique integer elements, write an
algorithm to create a binary search tree with minimal height.
'''


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


# review 1 code:
def minTree(a):
    _size = len(a)

    if _size == 0:
        return None

    midIndex = _size // 2
    midValue = a[midIndex]

    root = btreeNode(midValue)
    root.left = minTree(a[:midIndex])
    root.right = minTree(a[midIndex + 1:])

    return root


a = [0, 5, 7, 9, 10, 12, 13, 17]
resultTree = minHeight(a)
minT = minTree(a)
preOrderPrint(resultTree)
print("\n")
preOrderPrint(minT)
print("\n")
print(a)