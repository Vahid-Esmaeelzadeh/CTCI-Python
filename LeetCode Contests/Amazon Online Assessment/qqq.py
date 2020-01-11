def criticalRouters(numRouters, numLinks, links):
    # creating a dictionary to represent the graph
    g = {i: [] for i in range(numRouters)}
    for [i, j] in links:
        g[i - 1].append(j - 1)
        g[j - 1].append(i - 1)

    critical_routers = set()
    # at each  iteration, I want to remove one of the edges, and check the connectivity of graph
    # if it is not connected => the removed edge is a critical connection and the vertices are critical routeres

    for u, v in links:
        g[u - 1].remove(v - 1)
        g[v - 1].remove(u - 1)

        if not isConnected(g):
            critical_routers.add(u)
            critical_routers.add(v)

        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    return list(critical_routers)


def isConnected(graph):
    seen = {i: False for i in range(len(graph))}
    dfs(graph, seen, 0)

    for x in seen.values():
        if x is False:
            return False
    return True


def dfs(graph, seen, node):
    seen[node] = True
    for n in graph[node]:
        if seen[n] is False:
            dfs(graph, seen, n)


print(criticalRouters(6, 5, [[1,2], [2,3], [3,4], [4,5], [6,3]]))