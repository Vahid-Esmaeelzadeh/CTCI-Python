'''
Spiral copy
'''

import numpy


def spiral_copy(mat):
    if len(mat) == 0:
        return []

    rows = len(mat)
    cols = len(mat[0])

    result = []

    for j in range(cols):
        result.append(mat[0, j])

    for i in range(1, rows):
        result.append(mat[i, cols - 1])

    for j in range(cols - 2, -1, -1):
        if rows > 1:
            result.append(mat[rows - 1, j])

    for i in range(rows - 2, 0, -1):
        if cols > 1:
            result.append(mat[i, 0])

    return result + spiral_copy(mat[1:rows - 1, 1:cols - 1])


# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
a = [[1]]

a = numpy.array(a)
print()
print(spiral_copy(a))


# https://javabypatel.blogspot.com/2016/11/print-matrix-in-spiral-order-recursion.html
