'''
longest common subsequence
'''


def find_LCS_length(s1, s2):
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    return find_LCS_length_recursive(dp, s1, s2, 0, 0)


def find_LCS_length_recursive(dp, s1, s2, i1, i2):
    if i1 == len(s1) or i2 == len(s2):
        return 0

    if dp[i1][i2] == -1:
        if s1[i1] == s2[i2]:
            dp[i1][i2] = 1 + find_LCS_length_recursive(dp, s1, s2, i1 + 1, i2 + 1)
        else:
            c1 = find_LCS_length_recursive(dp, s1, s2, i1, i2 + 1)
            c2 = find_LCS_length_recursive(dp, s1, s2, i1 + 1, i2)
            dp[i1][i2] = max(c1, c2)

    return dp[i1][i2]


# tabulation with optimum space complexity
def find_LCS_length_tabulation(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(2)]

    for i in range(n1 - 1, -1, -1):
        for j in range(n2 - 1, -1, -1):
            if s1[i] == s2[j]:
                dp[i % 2][j] = 1 + dp[(i + 1) % 2][j + 1]
            else:
                dp[i % 2][j] = max(dp[(i + 1) % 2][j], dp[i % 2][j + 1])

    return max(dp[0][0], dp[1][0])  # I don't know which row has the latest update, so I return the maximum value simply


def main():
    print(find_LCS_length("abdca", "cbda"))
    print(find_LCS_length("passport", "ppsspt"))
    print()
    print(find_LCS_length_tabulation("abdca", "cbda"))
    print(find_LCS_length_tabulation("passport", "ppsspt"))

main()
