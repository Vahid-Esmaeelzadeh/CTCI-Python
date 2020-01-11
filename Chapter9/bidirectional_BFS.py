'''
Bidirectional BFS
'''

from collections import deque


class Node:
    def __init__(self, val=None, visited=False, neighbors=[]):
        self.val = val
        self.neighbors = neighbors
        self.visited = visited


def bi_bfs(src: Node, dst: Node):
    if src == dst:
        return True

    queue_s = deque()
    queue_d = deque()

    queue_s.append(src)
    src.visited = True

    queue_d.append(dst)
    dst.visited = True

    while queue_s and queue_d:
        s_node = queue_s.popleft()
        d_node = queue_d.popleft()

        if is_there_same_node(s_node.neighbors, d_node.neighbors) is True:
            return True

        for s in s_node.neighbors:
            if s.visited is False:
                if s == dst or s == d_node:
                    return True
                queue_s.append(s)

        for d in d_node.neighbors:
            if d.visited is False:
                if d == src or s_node:
                    return True
                queue_d.append(d)

    return False


def is_there_same_node(a, b):
    a_values = []
    for x in a:
        a_values.append(x.val)

    a_values.sort()

    for x in b:
        if binary_search(a_values, x.val) is True:
            return x

    return None


def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return True
        elif item < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.neighbors = [n2, n3]
n2.neighbors = [n1, n5]
n3.neighbors = [n1, n5]
n4.neighbors = [n6]
n5.neighbors = [n2, n3, n6]
n6.neighbors = [n4, n5]

print(bi_bfs(n2, n4))
