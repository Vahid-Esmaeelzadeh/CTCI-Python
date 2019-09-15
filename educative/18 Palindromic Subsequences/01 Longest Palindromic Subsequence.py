'''
Longest Palindromic Subsequence
'''


def find_LPS_length(st):
    memo = [[-1 for _ in range(len(st))] for _ in range(len(st))]
    return find_LPS_length_recursive(st, 0, len(st) - 1, memo)


def find_LPS_length_recursive(st, startIndex, endIndex, memo):
    if startIndex > endIndex:
        return 0

    # every sequence with one element is a palindrome of length 1
    if startIndex == endIndex:
        return 1

    if memo[startIndex][endIndex] != -1:
        return memo[startIndex][endIndex]

    # case 1: elements at the beginning and the end are the same
    if st[startIndex] == st[endIndex]:
        memo[startIndex][endIndex] = 2 + find_LPS_length_recursive(st, startIndex + 1, endIndex - 1, memo)
        return memo[startIndex][endIndex]

    # case 2: skip one element either from the beginning or the end
    c1 = find_LPS_length_recursive(st, startIndex + 1, endIndex, memo)
    c2 = find_LPS_length_recursive(st, startIndex, endIndex - 1, memo)

    memo[startIndex][endIndex] = max(c1, c2)

    return max(c1, c2)


def find_LPS_length_tabualtion(st):
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

def main():
    print(find_LPS_length("abdbca"))
    print(find_LPS_length("cddpd"))
    print(find_LPS_length("pqqp"))
    print()
    print(find_LPS_length_tabualtion("abdbca"))
    print(find_LPS_length_tabualtion("cddpd"))
    print(find_LPS_length_tabualtion("pqqp"))


main()
