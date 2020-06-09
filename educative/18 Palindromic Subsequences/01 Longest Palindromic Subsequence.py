'''
Longest Palindromic Subsequence
'''


def longest_palindromic_subsequence_length(st):
    memo = [[-1 for _ in range(len(st))] for _ in range(len(st))]
    ans = helper(st, 0, len(st) - 1, memo)
    # print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in memo]))
    return ans


def helper(st, i, j, memo):
    # base cases
    if i > j:
        return 0
    if i == j:
        return 1

    if memo[i][j] != -1:
        return memo[i][j]

    # case (I): first char is equal to the last char
    if st[i] == st[j]:
        memo[i][j] = 2 + helper(st, i + 1, j - 1, memo)
        return memo[i][j]
    # case (II)
    len1 = helper(st, i + 1, j, memo)  # skip a character from beginning
    len2 = helper(st, i, j - 1, memo)  # skip a character from end

    memo[i][j] = max(len1, len2)

    return max(len1, len2)


def longest_palindromic_subsequence_length_tabulation(st):
    n = len(st)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            if st[i] == st[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]


print(longest_palindromic_subsequence_length("abcdfba"))
print(longest_palindromic_subsequence_length("abbcbb"))
print(longest_palindromic_subsequence_length("accdda"))
print(longest_palindromic_subsequence_length("aaaaaaa"))
print(longest_palindromic_subsequence_length("abcdefg"))


print()

print(longest_palindromic_subsequence_length_tabulation("abcdfba"))
print(longest_palindromic_subsequence_length_tabulation("abbcbb"))
print(longest_palindromic_subsequence_length_tabulation("accdda"))
print(longest_palindromic_subsequence_length_tabulation("aaaaaaa"))
print(longest_palindromic_subsequence_length_tabulation("abcdefg"))
print("----")
print(longest_palindromic_subsequence_length_tabulation("cddpd"))