import math
def rotateMatrix(mat):
    n = len(mat)
    for i in range(math.ceil(n/2)):
        for j in range(i, n-i-1, 1):
            tmp = mat[i][j]
            mat[i][j] = mat[n-j-1][i]
            mat[n-j-1][i] = mat[n-i-1][n-j-1]
            mat[n-i-1][n-j-1] = mat[j][n-i-1]
            mat[j][n-i-1] = tmp


mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for r in mat:
    for c in r:
        print(c, end=" ")
    print()

rotateMatrix(mat)
print(mat)
for r in mat:
    for c in r:
        print(c, end=" ")
    print()
