'''
longest common substring
'''


def find_LCS_length(s1, s2):
    n1, n2 = len(s1), len(s2)
    maxLength = max(n1, n2)
    dp = [[[-1 for _ in range(maxLength)] for _ in range(n2)] for _ in range(n1)]
    memo = {}
    return find_LCS_length_recursive(memo, s1, s2, 0, 0, 0)


def find_LCS_length_recursive(dp, s1, s2, i1, i2, count):
    if i1 == len(s1) or i2 == len(s2):
        return count

    if (i1, i2, count) not in dp:
        c1 = count
        if s1[i1] == s2[i2]:
            c1 = find_LCS_length_recursive(dp, s1, s2, i1 + 1, i2 + 1, count + 1)
        c2 = find_LCS_length_recursive(dp, s1, s2, i1, i2 + 1, 0)
        c3 = find_LCS_length_recursive(dp, s1, s2, i1 + 1, i2, 0)

        dp[(i1, i2, count)] = max(c1, c2, c3)

    return dp[(i1, i2, count)]


def main():
    print(find_LCS_length("abdca", "cbda"))
    print(find_LCS_length("passport", "ppsspt"))


main()
