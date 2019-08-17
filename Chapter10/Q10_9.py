'''
Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in
ascending order, write a method to find an element.
'''


# region Solution (II) - optimal solution
def sorted_matrix_search(mat, x):
    if len(mat) == 0:
        return None

    src = Point(0, 0)
    dst = Point(len(mat) - 1, len(mat[0]) - 1)
    return find_element_in_sorted_matrix(mat, src, dst, x)


def find_element_in_sorted_matrix(mat, src, dst, x):
    # check if src or dst is out of bounds of matrix
    if src.in_bound(mat) is False or dst.in_bound(mat) is False:
        return None
    if mat[src.row][src.col] == x:
        return src
    elif src.is_before(dst) is False:
        return None

    # start = start of diagonal
    # end = end of diagonal
    # since the grid may not be square, the end of the diagonal may not equal dst.

    start = Point(src.row, src.col)
    diag_length = min(dst.row - src.row, dst.col - src.col)
    end = Point(src.row + diag_length, src.col + diag_length)

    # do the binary search on diagonal (finding the first element > x)
    mid_point = Point(0, 0)
    while start.is_before(end):
        mid_point.set_to_average(start, end)
        if x > mat[mid_point.row][mid_point.col]:
            start.row = mid_point.row + 1
            start.col = mid_point.col + 1
        else:
            end.row = mid_point.row - 1
            end.col = mid_point.col - 1
    '''
    # Now, start is equal to the value of pivot    
    Example: we want to find x = 4
    1 2  3  4 5
    2 3  4  5 6
    3 4 '5' 6 7
    4 5  6  7 8
    start will be equal to (2,2)
    '''

    # Split the grid to quadrants. Search the bottom left and the top right
    return split_and_search(mat, src, dst, start, x)


def split_and_search(mat, src, dst, pivot, x):

    lower_left_origin = Point(pivot.row, src.col)
    lower_left_dest = Point(dst.row, pivot.col - 1)
    upper_right_origin = Point(src.row, pivot.col)
    upper_right_dest = Point(pivot.row - 1, dst.col)

    lower_left = find_element_in_sorted_matrix(mat, lower_left_origin, lower_left_dest, x)
    if lower_left is None:
        return find_element_in_sorted_matrix(mat, upper_right_origin, upper_right_dest, x)
    return lower_left


class Point:
    def __init__(self, r, c):
        self.row = r
        self.col = c

    def in_bound(self, mat):
        return 0 <= self.row < len(mat) and 0 <= self.col < len(mat[0])

    def is_before(self, p):
        return self.row <= p.row and self.col <= p.col

    def set_to_average(self, p, q):
        self.row = (p.row + q.row) // 2
        self.col = (p.col + q.col) // 2

# endregion



# region My solution
def matrix_search(mat, x):
    m = len(mat)
    if m == 0:
        return None
    n = len(mat[0])

    return matrix_search_rcr(mat, x, m - 1, n - 1)


def matrix_search_rcr(mat, x, m, n):
    if m < 0 or n < 0:
        return None

    if x < mat[0][0] or x > mat[m][n]:
        return None

    if x == mat[m][n]:
        return [m, n]

    result = matrix_search_rcr(mat, x, m - 1, n - 1)
    if result:
        return result

    res_col = binary_search_in_col(mat, x, n)
    if res_col:
        return res_col

    res_row = binary_search_in_row(mat, x, m)
    if res_row:
        return res_row

    return None


def binary_search_in_col(mat, x, c):
    start = 0
    end = len(mat) - 2

    while start <= end:
        mid = (start + end) // 2
        if x == mat[mid][c]:
            return [mid, c]
        if x > mat[mid][c]:
            start = mid + 1
        elif x < mat[mid][c]:
            end = mid - 1

    return None


def binary_search_in_row(mat, x, r):
    left = 0
    if len(mat) > 0:
        right = len(mat[0]) - 2
    else:
        return None

    while left <= right:
        mid = (left + right) // 2
        if x == mat[r][mid]:
            return [r, mid]
        if x > mat[r][mid]:
            left = mid + 1
        elif x < mat[r][mid]:
            right = mid - 1

    return None
# endregion


# region Solution (I)
def find_element(mat, x):
    row = 0
    if len(mat) == 0:
        return None
    col = len(mat[0]) - 1

    while row < len(mat) and col >= 0:
        if mat[row][col] == x:
            return [row, col]
        if x < mat[row][col]:
            col -= 1
        if x > mat[row][col]:
            row += 1

    return None
# endregion


a = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21]]
print(matrix_search(a, 20))
print(find_element(a, 20))
z = sorted_matrix_search(a, 20)
print([z.row, z.col])