'''
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.

BFS & DFS
DFS & BFS
'''

from enum import Enum
from collections import deque
import copy


class Node:
    def __init__(self, name, adjacent: list = []):
        self.name = name
        self.adjacentlist = adjacent
        self.state = False  # False for unvisited, True for visited


class Graph:
    def __init__(self, nodes: list = []):
        self.nodes = nodes


def searchDFS(start):
    if start is None:
        return

    print(start.name, end=' ')
    start.state = True

    for v in start.adjacentlist:
        if v.state is False:
            searchDFS(v)


# DFS in graph
def isThereRoute_DFS(start, end):
    if (start is None) or (end is None):
        return False

    print(start.name, end=" ")
    if start == end:
        return True

    start.state = True

    for v in start.adjacentlist:
        if v.state is False:
            if isThereRoute_DFS(v, end):
                return True

    return False


def searchBFS(start: Node):
    q = deque()
    start.state = True
    q.append(start)

    while q:
        n = q.popleft()
        print(n.name, end=' ')
        for v in n.adjacentlist:
            if v.state is False:
                v.state = True
                q.append(v)


# BFS in graph
def isThereRoute_BFS(start: Node, end: Node):
    if start == end:
        return [True, 0]  # length of path

    path_len = 0
    q = deque()
    start.state = True
    q.append(start)

    while len(q) != 0:
        n = q.popleft()
        print(n.name, end=' ')
        path_len += 1

        for v in n.adjacentlist:
            if v.state is False:
                if v == end:
                    return [True, path_len]
                v.state = True
                q.append(v)

    return [False, -1]

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

# searchDFS(nodes[0])
# print()
# print(isThereRoute_DFS(nodes[0], nodes[7]))
# print()
# searchBFS(nodes[0])
print(isThereRoute_BFS(nodes[0], nodes[7]))

