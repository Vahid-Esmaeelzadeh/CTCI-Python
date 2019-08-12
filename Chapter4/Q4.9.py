'''
BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.

EXAMPLE
Input:
        2
      /   \
     1     3

Output: {2, 1, 3}, {2, 3, 1}
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def BSTsequences(root: Node):
    if root is None:
        return [[]]

    sequences = []
    prefix = root.data

    left_sequences = BSTsequences(root.left)
    right_sequences = BSTsequences(root.right)

    for L in left_sequences:
        for R in right_sequences:
            weaved = []
            weaveLists([prefix], L, R, weaved)
            sequences += weaved

    return sequences


def weaveLists(prefix: list, first: list, second: list, results: [list]):
    if len(first) == 0 or len(second) == 0:
        results.append(prefix + first + second)
        return

    weaveLists(prefix + [first[0]], first[1:], second, results)
    weaveLists(prefix + [second[0]], first, second[1:], results)


root = Node(4)
root.left = Node(2)
root.right = Node(6)

root.left.left = Node(1)
root.left.right = Node(3)

root.right.left = Node(5)
root.right.right = Node(7)


seq = BSTsequences(root)
for x in seq:
    print(x)

print(len(seq))
