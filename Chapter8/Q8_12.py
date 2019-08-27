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

import copy

# region Question 8.12 (8 queens - CTCI solution)
GRID_SIZE = 8


def placeQueens(row, columns, results):
    if row == GRID_SIZE:
        results.append(columns)
    else:
        for col in range(GRID_SIZE):
            if checkValid(columns, row, col):
                columns[row] = col
                placeQueens(row+1, columns[:], results)


def checkValid(columns, row1, column1):
    for row2 in range(row1):
        column2 = columns[row2]

        if column1 == column2:
            return False
        if abs(column2-column1) == (row1-row2):
            return False

    return True
# endregion


columns = [None for _ in range(8)]
results = []

placeQueens(0, columns, results)
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
    #chess1 = chess[:]
    chess1[cell] = -1
    # update the chess if we use the smallest cell
    chess2 = updateChess(chess, cell)
    return queens(n, chess1) + queens(n-1, chess2)


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
            if i == row or j == col or abs(i-row) == abs(j-col):
                chess2[(i, j)] = -1
    return chess2


def find_smallest_cell(chess):
    for i in range(8):
        for j in range(8):
            if chess[(i, j)] == 0:
                return (i, j)


chess = {(x, y): 0 for x in range(8) for y in range(8)}

#print(queens(8, chess))
print(chess)

# endregion


# FINAL REVIEW NEEDED


