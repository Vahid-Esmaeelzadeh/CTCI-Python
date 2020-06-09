'''
longest palindromic substring
'''


def find_LPS_length(st):
    return helper(st, 0, len(st) - 1)


def helper(st, i, j):
    # base cases
    if i > j:
        return 0
    if i == j:
        return 1

    # case (I): first char is equal to the last char
    if st[i] == st[j]:
        remaining_len = j - i - 1
        # check if the remaining string is also a palindrome
        if remaining_len == helper(st, i + 1, j - 1):
            return remaining_len + 2

    # case (II)
    c1 = helper(st, i + 1, j)  # skip a character from beginning
    c2 = helper(st, i, j - 1)  # skip a character from end
    return max(c1, c2)


def find_LPS_length_memo(st):
    n = len(st)
    memo = [[-1 for _ in range(n)] for _ in range(n)]
    return helper_memo(memo, st, 0, n - 1)


def helper_memo(memo, st, i, j):
    if i > j:
        return 0
    if i == j:
        return 1

    if memo[i][j] == -1:
        # case (I): first char is equal to the last char
        if st[i] == st[j]:
            remaining_len = j - i - 1
            # check if the remaining substring is palindromic
            if remaining_len == helper_memo(memo, st, i + 1, j - 1):
                memo[i][j] = remaining_len + 2
                return memo[i][j]

        # case (II)
        c1 = helper_memo(memo, st, i + 1, j)  # skip a character from beginning
        c2 = helper_memo(memo, st, i, j - 1)  # skip a character from end
        memo[i][j] = max(c1, c2)

    return memo[i][j]


def main():
    print(find_LPS_length("abdbca"))
    print(find_LPS_length("cddpd"))
    print(find_LPS_length("pqr"))


main()
