'''
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
'''


def rotate90(mat: list):
    n = len(mat)

    if n == 0 or n != len(mat[0]):
        return False

    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first

            # save top
            top = mat[first][i]

            # top <- left   (top row: col is variable, row is fixed = first)
            mat[first][i] = mat[last-offset][first]

            # left <- bottom (left col: row is variable, col is fixed = first)
            mat[last-offset][first] = mat[last][last-offset]

            # bottom <- right (bottom row: col is variable, row is fixed = last)
            mat[last][last-offset] = mat[i][last]

            # right <- top (right col: row is variable, col is fixed = last)
            mat[i][last] = top

    return True


def rotate(mat: list, degree: int):
    if degree % 90 != 0:
        print("Error in the value of degree! It should be a multiple of 90.\n")
        return

    degree = degree % 360
    if degree < 0:
        degree += 360

    for i in range(degree // 90):
        rotate90(mat)


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


# print()
# rotate(a, -270)
# for x in a:
#     print(x)

print()
rotate90(a)
for x in a:
    print(x)
