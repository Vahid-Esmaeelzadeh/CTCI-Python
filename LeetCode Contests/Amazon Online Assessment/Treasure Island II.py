'''
You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs.
Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a
shortest route to one of the treasure islands.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from one of the
starting point (marked as S) of the map and can move one block up, down, left or right at a time. The treasure island
is marked as X. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks.
You cannot leave the map area. Other areas O are safe to sail in. Output the minimum number of steps to get to any of
the treasure islands.

Example:

Input:
[['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

Output: 3
Explanation:
You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0).
Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).
'''


from collections import deque

def shortest_path(grid):
    rows, cols = len(grid), len(grid[0])

    queue = deque()

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                queue.append([i, j, 0])
                grid[i][j] = 'D'  # visited, it means we cannot enter it again

    while queue:
        r, c, length = queue.popleft()

        for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if 0 <= r+dr < rows and 0 <= c+dc < cols:
                if grid[r+dr][c+dc] == 'X':
                    return length + 1
                if grid[r+dr][c+dc] == 'O':
                    grid[r+dr][c+dc] = 'D'  # visited, it means we cannot enter it again
                    queue.append([r+dr, c+dc, length+1])
    return -1


grid = [['S', 'O', 'O', 'S', 'S'],
         ['D', 'O', 'D', 'O', 'D'],
         ['O', 'O', 'O', 'O', 'X'],
         ['X', 'D', 'D', 'O', 'O'],
         ['X', 'D', 'D', 'D', 'O']]

print(shortest_path(grid))