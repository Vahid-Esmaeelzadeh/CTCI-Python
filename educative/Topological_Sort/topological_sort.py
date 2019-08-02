'''
Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices
such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.
'''

# region my implementation
def topological_sort(vertices, edges):
    sorted_order = []
    adj_dict = convert_to_adj_dict(vertices, edges)

    while len(adj_dict) > 0:
        root_vertices = extract_root_vertices(adj_dict)

        if len(root_vertices) == 0:
            break

        for x in root_vertices:
            sorted_order.append(x)
            del adj_dict[x]

    return sorted_order


def convert_to_adj_dict(vertices, edges):
    adj_dict = {}

    for i in range(vertices):
        adj_dict[i] = []

    for v1, v2 in edges:
        adj_dict[v1].append(v2)

    return adj_dict
# endregion

# educative.io implementation
from collections import deque


def topological_sort2(vertices, edges):
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder

    # a. Initialize the graph
    inDegree = {i: 0 for i in range(vertices)}  # count of incoming edges
    graph = {i: [] for i in range(vertices)}  # adjacency list graph

    # b. Build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)  # put the child into it's parent's list
        inDegree[child] += 1  # increment child's inDegree

    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:  # get the node's children to decrement their in-degrees
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has a cycle
    if len(sortedOrder) != vertices:
        return []

    return sortedOrder

# endregion

def extract_root_vertices(adj_dict):
    vertices = set(adj_dict.keys())
    dependent_vertices = set()
    for row in adj_dict:
        for x in adj_dict[row]:
            dependent_vertices.add(x)

    return vertices - dependent_vertices





def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
