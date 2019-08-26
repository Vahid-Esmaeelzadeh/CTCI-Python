'''
shortest path
shortest path len
'''

from collections import deque


def shortest_path_len(grid, sr, sc, tr, tc):
    R = len(grid)
    C = len(grid[0])

    seen = [[False for _ in range(C)] for _ in range(R)]
    queue = deque()
    count = 0

    queue.append([sr, sc, count])
    seen[sr][sc] = True

    while queue:
        sr, sc, count = queue.popleft()

        if sr == tr and sc == tc:
            return count

        if 0 <= sr < R and 0 <= sc + 1 < C and grid[sr][sc+1] == 1 and seen[sr][sc+1] is False:
            queue.append([sr, sc + 1, count + 1])
            seen[sr][sc + 1] = True

        if 0 <= sr < R and 0 <= sc - 1 < C and grid[sr][sc-1] == 1 and seen[sr][sc-1] is False:
            queue.append([sr, sc - 1, count + 1])
            seen[sr][sc - 1] = True

        if 0 <= sr - 1 < R and 0 <= sc < C and grid[sr-1][sc] == 1 and seen[sr-1][sc] is False:
            queue.append([sr-1, sc, count + 1])
            seen[sr - 1][sc] = True

        if 0 <= sr + 1 < R and 0 <= sc < C and grid[sr+1][sc] == 1 and seen[sr+1][sc] is False:
            queue.append([sr+1, sc, count + 1])
            seen[sr + 1][sc] = True

    return -1


def shortest_path(grid, sr, sc, tr, tc):
    R = len(grid)
    C = len(grid[0])

    queue = deque()
    seen = [[False for _ in range(C)] for _ in range(R)]

    queue.append([sr, sc, [(sr, sc)]])
    seen[sr][sc] = True

    while queue:
        [sr, sc, current_path] = queue.popleft()

        if sr == tr and sc == tc:
            return current_path

        if 0 <= sr < R and 0 <= sc + 1 < C and grid[sr][sc+1] == 1 and seen[sr][sc+1] is False:
            queue.append([sr, sc + 1, current_path + [(sr, sc + 1)]])
            seen[sr][sc + 1] = True

        if 0 <= sr < R and 0 <= sc - 1 < C and grid[sr][sc-1] == 1 and seen[sr][sc-1] is False:
            queue.append([sr, sc - 1, current_path + [(sr, sc - 1)]])
            seen[sr][sc - 1] = True

        if 0 <= sr - 1 < R and 0 <= sc < C and grid[sr-1][sc] == 1 and seen[sr-1][sc] is False:
            queue.append([sr - 1, sc, current_path + [(sr - 1, sc)]])
            seen[sr - 1][sc] = True

        if 0 <= sr + 1 < R and 0 <= sc < C and grid[sr+1][sc] == 1 and seen[sr+1][sc] is False:
            queue.append([sr + 1, sc, current_path + [(sr + 1, sc)]])
            seen[sr + 1][sc] = True

    return []


grid = [[1, 1, 1, 1],
        [0, 1, 0, 1],
        [1, 1, 1, 1]]

print(shortest_path_len(grid, 0, 0, 2, 3))
print(shortest_path(grid, 0, 0, 2, 3))

