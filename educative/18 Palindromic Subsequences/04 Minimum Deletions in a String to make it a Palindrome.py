'''
Minimum Deletions in a String to make it a Palindrome
'''


def find_minimum_deletions(st):
    return len(st) - find_LPS_length(st)


def find_LPS_length(st):
    memo = [[-1 for _ in range(len(st))] for _ in range(len(st))]
    return find_LPS_length_recursive(st, 0, len(st) - 1, memo)


def find_LPS_length_recursive(st, startIndex, endIndex, memo):
    if startIndex > endIndex:
        return 0

    # every sequence with one element is a palindrome of length 1
    if startIndex == endIndex:
        return 1

    if memo[startIndex][endIndex] == -1:
        # case 1: elements at the beginning and the end are the same
        if st[startIndex] == st[endIndex]:
            memo[startIndex][endIndex] = 2 + find_LPS_length_recursive(st, startIndex + 1, endIndex - 1, memo)
            return memo[startIndex][endIndex]

        # case 2: skip one element either from the beginning or the end
        c1 = find_LPS_length_recursive(st, startIndex + 1, endIndex, memo)
        c2 = find_LPS_length_recursive(st, startIndex, endIndex - 1, memo)

        memo[startIndex][endIndex] = max(c1, c2)

    return memo[startIndex][endIndex]


def main():
    print(find_minimum_deletions("abdbca"))
    print(find_minimum_deletions("cddpd"))
    print(find_minimum_deletions("pqr"))


main()
