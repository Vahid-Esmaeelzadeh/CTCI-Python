'''
785. Is Graph Bipartite?
'''
from collections import deque

def isBipartite(graph):
    # initialize the partite with 0 for each vertex
    partite = [0 for _ in range(len(graph))]

    queue = deque()
    queue.append((0, 1))
    partite[0] = 1  # -1 , +1 for partitis

    # seen = set()
    # seen.add(0)
    unseen = set(range(len(graph)))
    unseen.remove(0)

    while queue:
        current_node, part = queue.popleft()

        for neighbor in graph[current_node]:
            if neighbor in unseen:
                queue.append((neighbor, -part))
                partite[neighbor] = -part
                unseen.remove(neighbor)
            else:
                if partite[neighbor] != -part:
                    return [False, partite]

        if len(queue) == 0 and len(unseen) > 0:
            new_vertex = unseen.pop()
            queue.append((new_vertex, 1))
            partite[new_vertex] = 1

    return [True, partite]


g = [[1, 3],
     [0, 2],
     [1, 3],
     [0, 2]]

g1 = [[1, 2, 3],
      [0, 2],
      [0, 1, 3],
      [0, 2]]

g2 = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
g3 = [[1,2,3],[0,2],[0,1,3],[0,2]]
print(isBipartite(g))
print(isBipartite(g1))
print(isBipartite(g2))
print(isBipartite(g3))