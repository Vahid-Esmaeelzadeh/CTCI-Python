# Uncrossed Lines

def maxUncrossedLines(A: list, B: list) -> int:
    return helper(A, B, 0, 0, {})


def helper(A: list, B: list, i, j, memo):
    if i == len(A) or j == len(B):
        return 0

    if (i, j) in memo:
        return memo[(i,j)]
    # skip A[i]
    c1 = helper(A, B, i + 1, j, memo)

    # connect A[i] to first possible B[j]
    # cross_j_index = -1
    # for b_ind in range(j, len(B)):
    #     if A[i] == B[b_ind]:
    #         cross_j_index = b_ind
    #         break
    try:
        cross_j_index = B.index(A[i], j, len(B))
    except ValueError:
        cross_j_index = -1

    c2 = 0
    if cross_j_index != -1:
        c2 = 1 + helper(A, B, i + 1, cross_j_index + 1, memo)

    memo[(i, j)] = max(c1, c2)
    return memo[(i, j)]


A = [2,5,1,2,5]
B = [10,5,2,1,5,2]

A = [1,3,7,1,7,5]
B = [1,9,2,5,1]

print(maxUncrossedLines(A, B))
print(B.index(1))