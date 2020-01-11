'''
1129 Shortest Path with Alternating Colors

Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and
there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges
denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X
such that the edge colors alternate along the path (or -1 if such a path doesn't exist).


Example 1:
Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]

Example 2:
Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]

Example 3:
Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]

Example 4:
Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]

Example 5:
Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]
'''

import math
from collections import deque


def shortest_path(red_edges, blue_edges, n):
    # build the graph in hash table
    graph = {i: [[], []] for i in range(n)}  # node: [red edges list], [blue edges list]
    for [i, j] in red_edges:
        graph[i][0].append(j)
    for [i, j] in blue_edges:
        graph[i][1].append(j)

    res = [math.inf for _ in range(n)]
    res[0] = 0
    min_len = 0

    queue = deque()
    queue.append((0, "r"))
    queue.append((0, "b"))

    seen = set()

    while queue:
        level_size = len(queue)
        min_len += 1

        for _ in range(level_size):
            node, color = queue.popleft()

            if (node, color) not in seen:
                seen.add((node, color))

                # add all opposite color children in the queue
                if color == "r":
                    for child in graph[node][1]:
                        queue.append((child, "b"))
                        res[child] = min(min_len, res[child])
                if color == "b":
                    for child in graph[node][0]:
                        queue.append((child, "r"))
                        res[child] = min(min_len, res[child])

    for i in range(n):
        if res[i] == math.inf:
            res[i] = -1

    return res


red_edges = [[0, 1], [1, 2], [2, 3], [2, 1], [3, 4]]
blue_edges = [[1, 2], [2, 3], [3, 1]]
n = 5

print(shortest_path(red_edges, blue_edges, n))
