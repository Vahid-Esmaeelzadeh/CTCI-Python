'''
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
'''


class Solution:
    def searchMatrix(self, matrix, target):
        n_row = len(matrix)
        n_col = len(matrix[0])

        end = [n_row - 1, n_col - 1]
        if n_row < n_col:
            start = [0, n_col - n_row]
        else:
            start = [n_row - n_col, 0]

        pivot, found = self.diagonal_binary_search(matrix, target, start, end)
