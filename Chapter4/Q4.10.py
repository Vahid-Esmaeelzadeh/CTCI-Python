'''
Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorithm to determine if T2 is a subtree of Tl.

A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# region Solution1
def isSubTree(T1: Node, T2: Node) -> bool:
    s1 = preOrderString(T1)
    s2 = preOrderString(T2)

    print(s1)
    print(s2)

    if s2 in s1:
        return True
    return False


def preOrderString(n: Node):
    if n is None:
        return "X"
    return str(n.data) + " " + preOrderString(n.left) + preOrderString(n.right)
# endregion

# region Solution2
def containsTree(T1: Node, T2: Node):
    if T2 is None:
        return True
    if T1 is None:
        return False
    if T1.data == T2.data and matchTree(T1, T2):
        return True
    return containsTree(T1.left, T2) or containsTree(T1.right, T2)


def matchTree(T1, T2):
    if T1 is None and T2 is None:
        return True
    if T1 is None or T2 is None:
        return False
    if T1.data != T2.data:
        return False
    return matchTree(T1.left, T2.left) and matchTree(T1.right, T2.right)
# endregion


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
print(containsTree(T1, T2))

