'''
Palindromic Partitioning

Given a string, we want to cut it into pieces such that each piece is a palindrome. Write a function to return the
minimum number of cuts needed.

Input: "abdbca"
Output: 3
Explanation: Palindrome pieces are "a", "bdb", "c", "a".
'''


def find_MPP_cuts(st):
    return find_MPP_cuts_recursive(st, 0, len(st) - 1)


def find_MPP_cuts_recursive(st, startIndex, endIndex):
    # we don't need to cut the string if it is a palindrome
    if startIndex >= endIndex or is_palindrome(st, startIndex, endIndex):
        return 0

    # at max, we need to cut the string into its 'length-1' pieces
    minimumCuts = endIndex - startIndex
    for i in range(startIndex, endIndex + 1):
        if is_palindrome(st, startIndex, i):
            # we can cut here as we have a palindrome from 'startIndex' to 'i'
            minimumCuts = min(
                minimumCuts, 1 + find_MPP_cuts_recursive(st, i + 1, endIndex))

    return minimumCuts


def is_palindrome(st, x, y):
    while x < y:
        if st[x] != st[y]:
            return False
        x += 1
        y -= 1
    return True


def main():
    print(find_MPP_cuts("abdbca"))
    print(find_MPP_cuts("cdpdd"))
    print(find_MPP_cuts("pqr"))
    print(find_MPP_cuts("pp"))
    print(find_MPP_cuts("madam"))


main()
