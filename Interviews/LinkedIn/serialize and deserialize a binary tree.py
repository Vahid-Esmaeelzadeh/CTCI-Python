'''
Serialize and deserialize a binary tree
'''
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def serialize(root):
    q = deque()
    q.append(root)
    result = []
    while q:
        node = q.popleft()
        if node is None:
            result.append("None")
            continue  # there is no children, so we should continue without adding any children
        else:
            result.append(node.val)
        q.append(node.left)
        q.append(node.right)
    return result


def deserialize(data):
    if not data or data[0] == 'None':
        return None
    q = deque()
    root = Node(data[0])
    q.append(root)
    i = 1
    while q and i < len(data):
        node = q.popleft()
        if data[i] != 'None':
            node.left = Node(data[i])
            q.append(node.left)
        i += 1
        if data[i] != 'None':
            node.right = Node(data[i])
            q.append(node.right)
        i += 1
    return root



T1 = Node(4)
T1.left = Node(2)
T1.right = Node(6)

T1.left.left = Node(1)
T1.left.right = Node(3)

T1.right.left = Node(5)
T1.right.right = Node(7)

print(preOrderString(T1))
