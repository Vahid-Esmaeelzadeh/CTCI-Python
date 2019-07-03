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


# region Solution (II)

# endregion
a = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21]]
print(matrix_search(a, 20))
print(find_element(a, 20))