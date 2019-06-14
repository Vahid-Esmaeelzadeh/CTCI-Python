class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

# region Solution 1
def firstCommonAncestor1(n1: Node, n2: Node):
    if n1 is None or n2 is None:
        return None

    d1, d2 = 0, 0
    runner1 = n1
    runner2 = n2

    while runner1 is not None:
        runner1 = runner1.parent
        d1 += 1

    while runner2 is not None:
        runner2 = runner2.parent
        d2 += 1

    diff = d1 - d2
    deeper = None
    shallower = None

    if diff > 0:
        deeper = n1
        shallower = n2
    else:
        deeper = n2
        shallower = n1

    diff = abs(diff)

    while diff > 0 and deeper is not None:
        deeper = deeper.parent
        diff -= 1

    while (deeper != shallower) and (deeper is not None) and (shallower is not None):
        deeper = deeper.parent
        shallower = shallower.parent

    return deeper
# endregion

# region Solution 2
def firstCommonAncestor2(root: Node, p: Node, q: Node):
    if (not covers(root, p)) or (not covers(root, q)):
        return None
    if covers(p, q):
        return p
    if covers(q, p):
        return q

    sibling = getSibling(p)
    parent = p.parent

    while not covers(sibling, q):
        sibling = getSibling(parent)
        parent = parent.parent

    return parent
def covers1(root: Node, n: Node):
    while (n is not None) and (root != n):
        n = n.parent

    if root == n:
        return True
    return False
def covers(root: Node, n: Node):
    if root is None:
        return False
    if root == n:
        return True
    return covers(root.left, n) or covers(root.right, n)
def getSibling(n: Node):
    if n is None or n.parent is None:
        return None

    if n.parent.left == n:  # n is the left child
        return n.parent.right

    if n.parent.right == n:
        return n.parent.left
# endregion

# region Solution 3 - without links to parents
def firstCommonAncestor3(root: Node, p: Node, q: Node):
    if (not covers(root, p)) or (not covers(root, q)):
        return None
    return commonAncestor_rcr(root, p, q)

def commonAncestor_rcr(root: Node, p: Node, q: Node):
    if root == p or root == q or root is None:
        return root

    p_in_left = covers(root.left, p)
    q_in_left = covers(root.left, q)

    if p_in_left != q_in_left:
        return root

    if p_in_left:
        return commonAncestor_rcr(root.left, p, q)
    return commonAncestor_rcr(root.right, p, q)
# endregion

# region Solution 4
# endregion

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
n3.left = None
n3.right = None

n4.parent = n2
n4.left = None
n4.right = None

n5.parent = n2
n5.left = n6
n5.right = n7

n6.parent = n5
n6.left = None
n6.right = None

n7.parent = n5
n7.left = None
n7.right = None

anc = firstCommonAncestor1(n4, n7)
if anc is not None:
    print(anc.data)
else:
    print("None")

anc = firstCommonAncestor2(n1, n4, n7)
if anc is not None:
    print(anc.data)
else:
    print("None")

anc = firstCommonAncestor3(n1, n4, n7)
if anc is not None:
    print(anc.data)
else:
    print("None")

