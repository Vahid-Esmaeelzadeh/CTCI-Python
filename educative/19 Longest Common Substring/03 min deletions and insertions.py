'''
minimum deletions and insertions to transform a string into another
'''


def find_MDI(s1, s2):
    c = LCSubSeq(s1, s2)
    return [len(s1) - c, len(s2) - c]  # [deletions, insertions]


def LCSubSeq(s1, s2):
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
    print(find_MDI("abc", "fbc"))
    print(find_MDI("abdca", "cbda"))
    print(find_MDI("passport", "ppsspt"))


main()
