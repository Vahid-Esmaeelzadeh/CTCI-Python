from numpy import *

def zeroMatrix1(A): # O(MN) space complexity
    mask = ones(shape(A))
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 0:
                mask[i, :] = 0
                mask[:, j] = 0

    for i in range(len(mask)):
        for j in range(len(mask[0])):
            if mask[i][j] == 0:
                A[i][j] = 0

def zeroMatrix2(A: array): # O(1) space complexity

    m = len(A)
    n = 0
    if m > 0:
        n = len(A[0])

    first_row_has_zero = ~all(A[0])
    first_col_has_zero = ~all(A[:, 0])

    #[i for (i, row) in enumerate(A) if not all(row)]
    for i in range(1, m):
        for j in range(1, n):
            if A[i, j] == 0:
                A[i][0] = 0
                A[0][j] = 0

    for i in range(1, m):
        if A[i][0] == 0:
            A[i, :] = [0]*n

    for j in range(1, n):
        if A[0][j] == 0:
            A[:, j] = transpose([0]*m)

    if first_row_has_zero:
        A[0, :] = [0]*n
    if first_col_has_zero:
        A[:, 0] = transpose([0]*m)

mat = array([[1, 2, 3, 4], [2, 0, -2, 1], [2, 2, 2, 2]])

print(mat)
zeroMatrix1(mat)
print(mat)

A = array([[1, 1, 3, 4], [2, 1, 0, 1], [2, 2, 2, 2]])
zeroMatrix2(A)
print(A)
