class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(root: Node):
    return isBST_rcr(root, None, None)

def isBST_rcr(root, _min, _max):
    if root is None:
        return True

    if (_min and root.data <= _min) or (_max and root.data > _max):
        return False

    isLeftBST = isBST_rcr(root.left, _min, root.data)
    isRightBST = isBST_rcr(root.right, root.data, _max)

    if isLeftBST and isRightBST:
        return True

    return False

root = Node(20)
root.left = Node(10)
root.right = Node(22)
root.left.left = Node(9)
root.left.right = Node(11)
root.right.left = Node(20)
root.right.right = Node(25)

print(isBST(root))
