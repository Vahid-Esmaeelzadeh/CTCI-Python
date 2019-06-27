import random


class Board:
    def __init__(self, n=10, bomb_num=8):
        self.board = []
        for i in range(n):
            self.board.append([" "] * n)

        self.initialize(bomb_num)

    def show(self):
        print("-" * (4 * len(self.board) + 1))
        for i in self.board:
            for j in i:
                print("|", j, end=" ")
            print("|", end="\n")
            print("-" * (4 * len(self.board) + 1))

    def is_indices_valid(self, i, j):
        n = len(self.board)
        return 0 <= i < n and 0 <= j < n

    def calc_cell_value(self, i, j):
        count = 0
        if self.board[i][j] != "x":
            count += 1 if self.is_indices_valid(i - 1, j - 1) and self.board[i - 1][j - 1] == "x" else 0
            count += 1 if self.is_indices_valid(i - 1, j) and self.board[i - 1][j] == "x" else 0
            count += 1 if self.is_indices_valid(i - 1, j + 1) and self.board[i - 1][j + 1] == "x" else 0
            count += 1 if self.is_indices_valid(i, j - 1) and self.board[i][j - 1] == "x" else 0
            count += 1 if self.is_indices_valid(i, j + 1) and self.board[i][j + 1] == "x" else 0
            count += 1 if self.is_indices_valid(i + 1, j - 1) and self.board[i + 1][j - 1] == "x" else 0
            count += 1 if self.is_indices_valid(i + 1, j) and self.board[i + 1][j] == "x" else 0
            count += 1 if self.is_indices_valid(i + 1, j + 1) and self.board[i + 1][j + 1] == "x" else 0
        return count

    def initialize(self, bomb_num):
        count = 0
        n = len(self.board)

        # locate bombs in random
        while count < bomb_num:
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            if self.board[i][j] != "x":
                self.board[i][j] = "x"
                count += 1
        # calculate the cell values
        for i in range(n):
            for j in range(n):
                self.board[i][j] = self.calc_cell_value(i, j) if self.calc_cell_value(i, j) > 0 else self.board[i][j]

b = Board(5, 2)
b.show()

