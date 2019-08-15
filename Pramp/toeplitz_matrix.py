'''
Toeplitz Matrix
'''


# region comparison solution
def isToeplitz(arr):
    rows = len(arr)
    if rows <= 1:
        return True
    cols = len(arr[0])

    r, c = 0, 0
    while c < cols:
        i, j = r + 1, c + 1
        while i < rows and j < cols:
            if arr[r][c] != arr[i][j]:
                return False
            i += 1
            j += 1
        c += 1

    r, c = 1, 0
    while r < rows:
        i, j = r + 1, c + 1
        while i < rows and j < cols:
            if arr[r][c] != arr[i][j]:
                return False
            i += 1
            j += 1
        r += 1

    return True
# endregion


# region using hash-map
def isToeplitz_hash_map(arr):
    hash_table = {}
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if r - c not in hash_table:
                hash_table[r - c] = arr[r][c]
            elif arr[r][c] != hash_table[r - c]:
                return False

    return True
# endregion


a = [[8],
     [8],
     [8],
     [6],
     [8]]

print(isToeplitz(a))
