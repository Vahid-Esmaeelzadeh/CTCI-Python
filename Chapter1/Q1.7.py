def rotate(mat: list, degree: int):
    if degree % 90 != 0:
        print("Error in the value of degree! It should be a multiple of 90.\n")
        return

    degree = degree % 360
    if degree < 0:
        degree += 360

    for i in range(degree // 90):
        rotate90(mat)


def rotate90(mat: list):
    n = len(mat)
    for i in range(n // 2):
        for j in range(i, n - i - 1, 1):
            tmp = mat[i][j]
            mat[i][j] = mat[n - j - 1][i]
            mat[n - j - 1][i] = mat[n - i - 1][n - j - 1]
            mat[n - i - 1][n - j - 1] = mat[j][n - i - 1]
            mat[j][n - i - 1] = tmp


def horizontalFlip(mat: list):
    rowNum = len(mat)
    colNum = len(mat[0]) if rowNum > 0 else 0

    for i in range(rowNum):
        for j in range(colNum // 2):
            tmp = mat[i][j]
            mat[i][j] = mat[i][colNum - 1 - j]
            mat[i][colNum - 1 - j] = tmp

def verticalFlip(mat: list):
    rowNum = len(mat)
    colNum = len(mat[0]) if rowNum > 0 else 0

    for i in range(rowNum // 2):
        for j in range(colNum):
            tmp = mat[i][j]
            mat[i][j] = mat[rowNum - 1 - i][j]
            mat[rowNum - 1 - i][j] = tmp



a = [['01', '02', '03', '04', '05'],
     ['06', '07', '08', '09', '10'],
     ['11', '12', '13', '14', '15'],
     ['16', '17', '18', '19', '20'],
     ['21', '22', '23', '24', '25']]

b = [['01', '02', '03', '04', '05'],
     ['06', '07', '08', '09', '10']]


for x in b:
    print(x)

print()
horizontalFlip(b)
for x in b:
    print(x)

print()
verticalFlip(b)
for x in b:
    print(x)


print()
rotate(a, -270)
for x in a:
    print(x)

print()
rotate90(a)
for x in a:
    print(x)
