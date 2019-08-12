'''
Sales Path

The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary).
The root is the company itself, and every node in the tree represents a car distributor that receives cars from
the parent node and ships them to its children nodes. The leaf nodes are car dealerships that sell cars direct
to consumers. In addition, every node holds an integer that is the cost of shipping a car to it.

A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, is called a
Sales Path. The cost of a Sales Path is the sum of the costs for every node in the path. For example, in the tree
above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode, write a function
getCheapestCost that calculates the minimal Sales Path cost in the tree.
'''

import sys


def get_cheapest_cost(rootNode):
    if rootNode is None:
        return -1

    n = len(rootNode.children)

    if n == 0:
        return rootNode.cost
    else:
        min_cost = sys.maxsize
        for x in rootNode.children:
            temp_cost = get_cheapest_cost(x)
            if temp_cost < min_cost:
                min_cost = temp_cost

    return min_cost + rootNode.cost


# A node
class Node:

    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None


root = Node(0)
root.children.append(Node(5))
root.children.append(Node(3))
root.children.append(Node(6))
root.children[1].children.append(Node(1))

print(get_cheapest_cost(root))
