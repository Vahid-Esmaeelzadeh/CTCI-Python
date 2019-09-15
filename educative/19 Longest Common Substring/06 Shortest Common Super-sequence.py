'''
Shortest Common Super-sequence
'''


def find_SCS_length(s1, s2):
    c = find_LCS_length(s1, s2)
    return len(s1) + len(s2) - c


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


def main():
    print(find_SCS_length("abcf", "bdcf"))
    print(find_SCS_length("dynamic", "programming"))


main()
