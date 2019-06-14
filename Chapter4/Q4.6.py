class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


def successor(n: Node):
    if n is None:
        return None

    if n.right is not None:
        return leftMostChild(n.right)

    i = n
    while (i.parent is not None) and (i.parent.right == i):  # until the node is the right child
        i = i.parent

    return i.parent

def leftMostChild(n: Node):
    while n.left is not None:
        n = n.left

    return n

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n1.parent = None
n1.left = n2
n1.right = n3

n2.parent = n1
n2.left = n4
n2.right = n5

n3.parent = n1
n3.left = n6
n3.right = n7

n4.parent = n2
n4.left = None
n4.right = None

n5.parent = n2
n5.left = None
n5.right = None

n6.parent = n3
n6.left = None
n6.right = None

n7.parent = n3
n7.left = None
n7.right = None


res = successor(n7)
if res is not None:
    print(res.data)
else:
    print("No successor! this is the last node of tree!")

