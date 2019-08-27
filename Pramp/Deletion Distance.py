'''
Deletion Distance

The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order
to get the same string. For instance, the deletion distance between "heat" and "hit" is 3
'''


def deletion_distance_basic(str1, str2):
    return len(str1) + len(str2) - 2 * len_of_common_subsequence(str1, str2, 0, 0)


def len_of_common_subsequence_recr(str1, str2, i, j):
    if i == len(str1) or j == len(str2):
        return 0
    if str1[i] == str2[j]:
        return 1 + len_of_common_subsequence_recr(str1, str2, i + 1, j + 1)
    return max(len_of_common_subsequence_recr(str1, str2, i + 1, j),
               len_of_common_subsequence_recr(str1, str2, i, j + 1))


def deletion_distance_dp(str1, str2):
    memo = [[-1 for j in range(len(str2))] for i in range(len(str1))]
    return len(str1) + len(str2) - 2 * len_of_common_subsequence(str1, str2, 0, 0, memo)


def len_of_common_subsequence(str1, str2, i, j, memo):
    if i == len(str1) or j == len(str2):
        return 0

    if memo[i][j] != -1:
        return memo[i][j]

    if str1[i] == str2[j]:
        memo[i][j] = 1 + len_of_common_subsequence(str1, str2, i + 1, j + 1, memo)
        return memo[i][j]

    memo[i][j] = max(len_of_common_subsequence(str1, str2, i + 1, j, memo),
                     len_of_common_subsequence(str1, str2, i, j + 1, memo))

    return memo[i][j]
