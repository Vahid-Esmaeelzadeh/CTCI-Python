# 5426. Reorder Routes to Make All Paths Lead to the City Zero


def minReorder(n, connections):
    g = {i: [] for i in range(n)}
    edges_set = set()

    for parent, child in connections:
        g[parent].append(child)
        g[child].append(parent)
        edges_set.add((parent, child))

    seen = [0 for _ in range(n)]
    return helper(0, g, edges_set, seen)


def helper(curNode, g, edges_set, seen):
    # if sum(seen) == len(g):
    #     return 0
    count = 0
    for x in g[curNode]:
        dir = (x, curNode) in edges_set
        if seen[curNode] == 0:
            if dir is False:
                count += 1
            seen[curNode] = 1
            count += helper(x, g, edges_set, seen)

    return count


n = 6
conn = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]

n1 = 5
conn1 = [[1, 0], [1, 2], [3, 2], [3, 4]]

n2 = 3
conn2 = [[1, 0], [2, 0]]

# print(minReorder(n, conn))
# print(minReorder(n1, conn1))
print(minReorder(n2, conn2))
