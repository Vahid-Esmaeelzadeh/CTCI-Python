'''
Clone graph
'''


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


def cloneGraph(node):
    nodes_map = {None: None}
    return cloneNode(node, nodes_map)


def cloneNode(node, nodes_map):
    if node not in nodes_map:
        copy = Node(node.val, None)
        nodes_map[node] = copy
        copy.neighbors = [cloneNode(n, nodes_map) for n in node.neighbors]
    return nodes_map[node]


def printGraph(node):
    seen = set()
    printGraphDFS(node, seen)


def printGraphDFS(node, seen):
    if node not in seen:
        print(node.val, end=" ")
        seen.add(node)
        for n in node.neighbors:
            printGraphDFS(n, seen)



node1 = Node(1, None)
node2 = Node(2, None)
node3 = Node(3, None)
node4 = Node(4, None)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

printGraph(node2)
print()
printGraph(cloneGraph(node2))