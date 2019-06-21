def rotate90(mat: list):
    n = len(mat)
    for i in range(n // 2):
        for j in range(i, n - i - 1, 1):
            tmp = mat[i][j]
            mat[i][j] = mat[n - j - 1][i]
            mat[n - j - 1][i] = mat[n - i - 1][n - j - 1]
            mat[n - i - 1][n - j - 1] = mat[j][n - i - 1]
            mat[j][n - i - 1] = tmp


a = [[0, 1, 2, 3, 4],
     [5, 6, 7, 8, 9],
     [10, 11, 12, 13, 14],
     [15, 16, 17, 18, 19],
     [20, 21, 22, 23, 24]]

for x in a:
    print(x)

print()
rotate90(a)
for x in a:
    print(x)

print()
rotate90(a)
for x in a:
    print(x)
