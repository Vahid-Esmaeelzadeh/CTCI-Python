'''
323	Number of Connected Components in an Undirected Graph
'''


def connected_components(graph):
    count = 0
    seen = set()
    for i in range(len(graph)):
        if i not in seen:
            helper(graph, i, seen)
            count += 1
            print()
    return count


def helper(graph, i, seen):
    print(i, end=" ")
    neighbors = graph[i]
    seen.add(i)

    for node in neighbors:
        if node not in seen:
            helper(graph, node, seen)


g = {0: [1, 3],
     1: [0, 2],
     2: [1],
     3: [0],
     4: [5],
     5: [4]}

print(connected_components(g))