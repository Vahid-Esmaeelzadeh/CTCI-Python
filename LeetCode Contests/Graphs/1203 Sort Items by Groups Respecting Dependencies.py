'''
1203. Sort Items by Groups Respecting Dependencies [Not completed !!!]
'''

from collections import deque


def sortItems(n, m, group, beforeItems):
    graph, in_degree, sources = build_graph(beforeItems, n)
    groups_table = build_groups(group, m)
    possible_nodes = deque(sources)

    sorted_order = []

    while possible_nodes:
        selected_node = possible_nodes.popleft()
        sorted_order.append(selected_node)
        selected_group = group[selected_node]

        if selected_group != -1:
            groups_table[selected_group].remove(selected_node)
            possible_nodes = deque(groups_table[selected_group])

        for child in graph[selected_node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

        if len(possible_nodes) == 0:
            possible_nodes = deque(set(sources) - set(sorted_order))


    if len(sorted_order) != n:
        return []

    return sorted_order


def build_graph(before_items, n):
    graph = {i: [] for i in range(n)}
    in_degree = [0 for _ in range(n)]

    for child in range(n):
        for parent in before_items[child]:
            graph[parent].append(child)
            in_degree[child] += 1

    sources = []
    for i in range(n):
        if in_degree[i] == 0:
            sources.append(i)

    return [graph, in_degree, sources]


def build_groups(group, m):
    groups = {i: set() for i in range(m)}

    for i in range(len(group)):
        group_id = group[i]
        if group_id != -1:
            groups[group_id].add(i)

    return groups


n = 8
m = 2
group = [-1, -1, 1, 0, 0, 1, 0, -1]
beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]

n = 5
m = 5
group = [2,0,-1,3,0]
beforeItems = [[2,1,3],[2,4],[],[],[]]


n = 4
m = 1
group = [-1,0,0,-1]
beforeItems = [[],[0],[1,3],[2]]

print(build_groups(group, m))
print(build_graph(beforeItems, n))
print(sortItems(n, m, group, beforeItems))