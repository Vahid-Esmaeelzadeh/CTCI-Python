'''
longest palindromic substring
'''


def find_LPS_length(st):
    return find_LPS_length_recursive(st, 0, len(st) - 1)


def find_LPS_length_recursive(st, startIndex, endIndex):
    if startIndex > endIndex:
        return 0

    # every string with one character is a palindrome
    if startIndex == endIndex:
        return 1

    # case 1: elements at the beginning and the end are the same
    if st[startIndex] == st[endIndex]:
        remainingLength = endIndex - startIndex - 1
        # check if the remaining string is also a palindrome
        if remainingLength == find_LPS_length_recursive(st, startIndex + 1, endIndex - 1):
            return remainingLength + 2

    # case 2: skip one character either from the beginning or the end
    c1 = find_LPS_length_recursive(st, startIndex + 1, endIndex)
    c2 = find_LPS_length_recursive(st, startIndex, endIndex - 1)
    return max(c1, c2)


def find_LPS_length_dp(st):
    n = len(st)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return find_LPS_length_recursive_dp(dp, st, 0, n - 1)


def find_LPS_length_recursive_dp(dp, st, startIndex, endIndex):
    if startIndex > endIndex:
        return 0

    # every string with one character is a palindrome
    if startIndex == endIndex:
        return 1

    if dp[startIndex][endIndex] == -1:
        # case 1: elements at the beginning and the end are the same
        if st[startIndex] == st[endIndex]:
            remainingLength = endIndex - startIndex - 1
            # if the remaining string is a palindrome too
            if remainingLength == find_LPS_length_recursive_dp(dp, st, startIndex + 1, endIndex - 1):
                dp[startIndex][endIndex] = remainingLength + 2
                return dp[startIndex][endIndex]

        # case 2: skip one character either from the beginning or the end
        c1 = find_LPS_length_recursive_dp(dp, st, startIndex + 1, endIndex)
        c2 = find_LPS_length_recursive_dp(dp, st, startIndex, endIndex - 1)
        dp[startIndex][endIndex] = max(c1, c2)

    return dp[startIndex][endIndex]

def main():
    print(find_LPS_length("abdbca"))
    print(find_LPS_length("cddpd"))
    print(find_LPS_length("pqr"))


main()
