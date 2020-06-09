# 37. Sudoku Solver


def solveSudoku(board):
    return helper(board, 0, 0)


def helper(board, i, j):
    if i == 9:
        return True

    # calculate next row and col
    next_i = (i + 1) if j == 8 else i
    next_j = (j + 1) % len(board)

    if board[i][j] != ' ':
        return helper(board, next_i, next_j)

    for num in "123456789":
        if is_valid(board, i, j, num):
            board[i][j] = num
            if helper(board, next_i, next_j):
                return True
            board[i][j] = ' '

    return False


def is_valid(board, row, col, num):
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)

    # for i in range(9):
    #     if (board[i][col] == num or
    #             board[row][i] == num or
    #             board[start_row + i // 3][start_col + i % 3] == num):
    #         return False

    for i in range(9):
        if board[i][col] == num:
            return False

    for j in range(9):
        if board[row][j] == num:
            return False

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

    return True


b = [["5", "3", " ", " ", "7", " ", " ", " ", " "],
     ["6", " ", " ", "1", "9", "5", " ", " ", " "],
     [" ", "9", "8", " ", " ", " ", " ", "6", " "],
     ["8", " ", " ", " ", "6", " ", " ", " ", "3"],
     ["4", " ", " ", "8", " ", "3", " ", " ", "1"],
     ["7", " ", " ", " ", "2", " ", " ", " ", "6"],
     [" ", "6", " ", " ", " ", " ", "2", "8", " "],
     [" ", " ", " ", "4", "1", "9", " ", " ", "5"],
     [" ", " ", " ", " ", "8", " ", " ", "7", "9"]]



print(solveSudoku(b))
for row in b:
    print(row)
