def numberAmazonTreasureTrucks(rows, column, grid):
    count = 0
    for r in range(rows):
        for c in range(column):
            if grid[r][c] == 1:
                helper(grid, rows, column, r, c)
                count += 1

    return count


def helper(grid, rows, column, r, c):
    if not (0 <= r < rows and 0 <= c < column) or grid[r][c] == 0:
        return

    grid[r][c] = 0
    helper(grid, rows, column, r, c - 1)
    helper(grid, rows, column, r, c + 1)
    helper(grid, rows, column, r - 1, c)
    helper(grid, rows, column, r + 1, c)


grid = [[1, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 0, 1, 1],
        [1, 1, 1, 1]]

print(numberAmazonTreasureTrucks(5, 4, grid))