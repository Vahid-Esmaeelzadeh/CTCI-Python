class BtreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBalancedTree(root: BtreeNode):
    if root is None:
        return True

    left_H = findHeight(root.left)
    right_H = findHeight(root.right)

    if abs(left_H-right_H) > 1:
        print("Max difference in heights is: ", abs(left_H-right_H))
        return False

    return isBalancedTree(root.left) and isBalancedTree(root.right)


def findHeight(n: BtreeNode):
    if n is None:
        return -1
    return 1 + max(findHeight(n.left), findHeight(n.right))

root = BtreeNode(10)
root.left = BtreeNode(20)
root.right = BtreeNode(15)
root.left.left = BtreeNode(3)
root.left.right = BtreeNode(0)
root.right.left = BtreeNode(100)
root.right.right = BtreeNode(-99)

root.right.left.left = BtreeNode(5)
root.right.left.left.right = BtreeNode(44)
root.right.left.left.right.left = BtreeNode(33)

print(isBalancedTree(root))
