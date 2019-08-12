'''
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
'''

from enum import Enum
from collections import deque
import copy



class State(Enum):
    Unvisited = -1
    Visiting = 0
    Visited = 1


class Node:
    def __init__(self, name, adjacent: list = []):
        self.name = name
        self.adjacentlist = adjacent
        self.state = State.Unvisited


class Graph:
    def __init__(self, nodes: list = []):
        self.nodes = nodes


def searchDFS(start: Node):
    if start is None:
        return

    print(start.name)
    start.state = State.Visited

    for v in start.adjacentlist:
        if v.state == State.Unvisited:
            searchDFS(v)


def isThereRoute_DFS(start: Node, end: Node):
    if (start is None) or (end is None):
        return False

    if start == end:
        return True

    print(start.name)
    start.state = State.Visited

    for v in start.adjacentlist:
        if v.state == State.Unvisited:
            if isThereRoute_DFS(v, end):
                return True

    return False


def searchBFS(start: Node):
    q = deque()
    start.state = State.Visited
    q.append(start)

    while len(q) != 0:
        n = q.popleft()
        print(n.name)
        for v in n.adjacentlist:
            if v.state == State.Unvisited:
                v.state = State.Visited
                q.append(v)


def isThereRoute_BFS(start: Node, end: Node):
    if start == end:
        return True

    q = deque()
    start.state = State.Visited
    q.append(start)

    while len(q) != 0:
        n = q.popleft()
        print(n.name)
        for v in n.adjacentlist:
            if v.state == State.Unvisited:
                if v == end:
                    return True
                v.state = State.Visited
                q.append(v)

    return False

g = Graph()
nodes = []

for i in range(8):
    nodes.append(Node(i))

nodes[0].adjacentlist = [nodes[1], nodes[5]]
nodes[1].adjacentlist = [nodes[4]]
nodes[2].adjacentlist = [nodes[1], nodes[3]]
nodes[3].adjacentlist = [nodes[6], nodes[7]]
nodes[4].adjacentlist = [nodes[5], nodes[6], nodes[7]]
nodes[5].adjacentlist = [nodes[1], nodes[2]]
nodes[6].adjacentlist = []
nodes[7].adjacentlist = []

g.nodes = nodes

print(isThereRoute_DFS(nodes[0], nodes[7]))
# print(isThereRoute_BFS(nodes[0], nodes[7]))

