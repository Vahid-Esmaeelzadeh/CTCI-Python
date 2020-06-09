'''
Eight Queens: Write an algorithm to print all ways of arranging eight queens on an 8x8 chess board
so that none of them share the same row, column, or diagonal. In this case, "diagonal" means all
diagonals, not just the two that bisect the board.

0 1 2 3 4 5 6 7
----------------
0 0 0 0 0 0 0 0 | 0
0 0 0 0 0 0 0 0 | 1
0 0 0 0 0 0 0 0 | 2
0 0 0 0 0 0 0 0 | 3
0 0 0 0 0 0 0 0 | 4
0 0 0 0 0 0 0 0 | 5
0 0 0 0 0 0 0 0 | 6
0 0 0 0 0 0 0 0 | 7
----------------
'''


# region Question 8.12 (8 queens - CTCI solution)
GRID_SIZE = 8


def placeQueens(row, queens, results):
    if row == GRID_SIZE:
        results.append(list(queens))
    else:
        for col in range(8):
            if is_valid(queens, row, col):
                queens[row] = col
                placeQueens(row + 1, queens, results)
                queens[row] = None


def is_valid(queens, row, col):
    for r in range(row):
        new_col = queens[r]

        if col == new_col:
            return False
        if abs(new_col - col) == (row - r):
            return False

    return True


# endregion


queens = [None for _ in range(8)]
results = []

placeQueens(0, queens, results)
print(len(results))

for s in results:
    print(*s)


# region my solution
def queens(n, chess):
    if n == 0:
        return 1
    if noWay(chess):
        return 0

    cell = find_smallest_cell(chess)
    # update the chess if we don't use the smallest cell
    chess1 = copy.deepcopy(chess)
    # chess1 = chess[:]
    chess1[cell] = -1
    # update the chess if we use the smallest cell
    chess2 = updateChess(chess, cell)
    return queens(n, chess1) + queens(n - 1, chess2)


def noWay(chess):
    for i in range(8):
        for j in range(8):
            if chess[(i, j)] == 0:
                return False

    return True


def updateChess(chess, cell):
    chess2 = copy.deepcopy(chess)
    row = cell[0]
    col = cell[1]

    for i in range(8):
        for j in range(8):
            if i == row or j == col or abs(i - row) == abs(j - col):
                chess2[(i, j)] = -1
    return chess2


def find_smallest_cell(chess):
    for i in range(8):
        for j in range(8):
            if chess[(i, j)] == 0:
                return (i, j)


chess = {(x, y): 0 for x in range(8) for y in range(8)}

# print(queens(8, chess))
print(chess)

# endregion


# FINAL REVIEW NEEDED
