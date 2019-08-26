'''
First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

# region Solution 1 - using parents - basic - going up from both nodes
def firstCommonAncestor1(n1: Node, n2: Node):
    if n1 is None or n2 is None:
        return None

    d1 = findDepth(n1)
    d2 = findDepth(n2)

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

    while diff > 0 and deeper:
        deeper = deeper.parent
        diff -= 1

    while deeper and shallower and (deeper != shallower):
        deeper = deeper.parent
        shallower = shallower.parent

    return deeper


def findDepth(n: Node):
    runner = n
    d = 0
    while runner:
        runner = runner.parent
        d += 1

    return d
# endregion - -  -  - going

# region Solution 2 - using parents - better performance - going up only from one node
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
def getSibling(n: Node):
    if n is None or n.parent is None:
        return None

    if n.parent.left == n:  # n is the left child
        return n.parent.right

    if n.parent.right == n:
        return n.parent.left
# endregion

# region Solution 3 - without links to parents
def covers(root: Node, n: Node):
    if root is None:
        return False
    if root == n:
        return True
    return covers(root.left, n) or covers(root.right, n)

def firstCommonAncestor3(root: Node, p: Node, q: Node):
    if (not covers(root, p)) or (not covers(root, q)):
        return None
    return firstCommonAncestor3_helper(root, p, q)

def firstCommonAncestor3_helper(root: Node, p: Node, q: Node):
    if root == p or root == q or root is None:
        return root

    p_in_left = covers(root.left, p)
    q_in_left = covers(root.left, q)

    if p_in_left != q_in_left:
        return root

    if p_in_left:
        return firstCommonAncestor3_helper(root.left, p, q)
    return firstCommonAncestor3_helper(root.right, p, q)
# endregion

# region Solution 4
    # I will do that later.
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

n10 = Node(10)
n10.parent = None


anc = firstCommonAncestor1(n3, n7)
if anc is not None:
    print(anc.data)
else:
    print("None")

anc = firstCommonAncestor2(n1, n4, n7)
if anc is not None:
    print(anc.data)
else:
    print("None")

anc = firstCommonAncestor3(n1, n5, n4)
if anc is not None:
    print(anc.data)
else:
    print("None")

