class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isSubTree(T1: Node, T2: Node) -> bool:

    s1 = []
    s2 = []

    preOrderString(T1, s1)
    preOrderString(T2, s2)

    if s1.count(s2):
        return True
    return False


def preOrderString(n: Node, sb: list):
    if n is None:
        sb.append("X")
        return
    sb.append(str(n.data))
    preOrderString(n.left, sb)
    preOrderString(n.right, sb)


T1 = Node(4)
T1.left = Node(2)
T1.right = Node(6)

T1.left.left = Node(1)
T1.left.right = Node(3)

T1.right.left = Node(5)
T1.right.right = Node(7)

T2 = Node(6)
T2.left = Node(5)
T2.right = Node(7)

print(isSubTree(T1, T2))
