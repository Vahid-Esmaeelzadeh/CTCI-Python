'''
Zambie in matrix

Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human
beings into zombies every hour. Find out how many hours does it take to infect all humans?
'''

from collections import deque


def zambieMatrix(grid):
    n_row, n_col = len(grid), len(grid[0])
    queue = deque()

    for r in range(n_row):
        for c in range(n_col):
            if grid[r][c] == 1:
                queue.append([r, c])

    hour = -1
    while queue:
        size = len(queue)
        for _ in range(size):
            r, c = queue.popleft()
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                if 0 <= r + dr < n_row and 0 <= c + dc < n_col:
                    if grid[r + dr][c + dc] == 0:
                        queue.append([r + dr, c + dc])
                        grid[r + dr][c + dc] = 1
        hour += 1

    return hour


grid1 = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

grid2 = [[1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1]]

print(zambieMatrix(grid1))
print(zambieMatrix(grid2))