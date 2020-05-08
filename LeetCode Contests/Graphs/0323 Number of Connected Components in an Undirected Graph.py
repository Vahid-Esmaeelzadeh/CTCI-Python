'''
323	Number of Connected Components in an Undirected Graph
'''


def connected_components(graph):
    count = 0
    seen = set()
    components = []

    for i in range(len(graph)):
        if i not in seen:
            current_component = []
            helper(graph, i, seen, current_component)
            components.append(current_component)

    return components


def helper(graph, i, seen, current_component):
    current_component.append(i)
    neighbors = graph[i]
    seen.add(i)

    for node in neighbors:
        if node not in seen:
            helper(graph, node, seen, current_component)


g = {0: [1, 3],
     1: [0, 2],
     2: [1],
     3: [0],
     4: [5, 6],
     5: [4],
     6: [4],
     7: []}

comps = connected_components(g)
print(comps)
print(len(comps))
