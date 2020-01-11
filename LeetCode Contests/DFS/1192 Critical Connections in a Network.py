'''
1192. Critical Connections in a Network
'''

import collections
class Solution:
    def criticalConnections(self, n, connections):
        # creating a dictionary to represent the graph
        graph = {i: [] for i in range(n)}
        for [i, j] in connections:
            graph[i].append(j)
            graph[j].append(i)

        critical_edges = []
        # at each  iteration, I want to remove one of the edges, and check the connectivity of graph
        # if it is not connected => the removed edge is a critical connection
        for u, v in connections:
            graph[u].remove(v)
            graph[v].remove(u)

            if not self.isConnected(graph):
                critical_edges.append([u, v])

            graph[u].append(v)
            graph[v].append(u)

        return critical_edges

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



n = 5
connections = [[0,1],[1,2],[2,0],[1,3],[2,4], [0,4]]

sol = Solution()
print(sol.criticalConnections(n, connections))

# creating a dictionary to represent the graph
g = {i: [] for i in range(1, numRouters + 1)}
for [i, j] in links:
    g[i].append(j)
    g[j].append(i)

critical_routers = []
# at each  iteration, I want to remove one of the edges, and check the connectivity of graph
# if it is not connected => the removed edge is a critical connection and the vertices are critical routeres

print(len(g))
for u, v in links:
    g[u].remove(v)
    g[v].remove(u)

    if not isConnected(g):
        critical_routers.append(u)
        critical_routers.append(v)

    g[u].append(v)
    g[v].append(u)

return critical_routers


def isConnected(graph):
    seen = {i: False for i in range(1, len(graph) + 1)}
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