def zeroMatrix(mat: list):
    rowNum = len(mat)
    colNum = len(mat[0]) if rowNum != 0 else 0

    if rowNum == 0 or colNum == 0:
        return

    firstRowHasZero = mat[0].count(0) > 0
    firstColHasZero = False

    for x in mat:
        if x[0] == 0:
            firstColHasZero = True
            break
    # use the first row and col to save the zero existence in rows and cols
    for i in range(1, rowNum):
        for j in range(1, colNum):
            if mat[i][j] == 0:
                mat[0][j] = 0
                mat[i][0] = 0

    # make zero the rows
    for i in range(1, rowNum):
        if mat[i][0] == 0:
            for j in range(1, colNum):
                mat[i][j] = 0

    # make zero the cols
    for j in range(1, colNum):
        if mat[0][j] == 0:
            for i in range(1, rowNum):
                mat[i][j] = 0

    # make zero the first row
    if firstRowHasZero:
        for j in range(colNum):
            mat[0][j] = 0

    # make zero the first col
    if firstColHasZero:
        for i in range(rowNum):
            mat[i][0] = 0


a = [[0, 2, 3, 4, 5],
     [4, 1, 6, 7, 7],
     [4, 7, 0, 6, 2],
     [1, 4, 5, 7, 8],
     [6, 6, 6, 6, 0]]

zeroMatrix(a)
for x in a:
    print(x)