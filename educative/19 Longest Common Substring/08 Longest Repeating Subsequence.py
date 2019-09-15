'''
Longest Repeating Subsequence
'''


def find_LRS_length(str):
    return find_LRS_length_recursive(str, 0, 0)


def find_LRS_length_recursive(str, i1, i2):
    if i1 == len(str) or i2 == len(str):
        return 0

    if i1 != i2 and str[i1] == str[i2]:
        return 1 + find_LRS_length_recursive(str, i1 + 1, i2 + 1)

    c1 = find_LRS_length_recursive(str, i1, i2 + 1)
    c2 = find_LRS_length_recursive(str, i1 + 1, i2)

    return max(c1, c2)


def main():
    print(find_LRS_length("tomorrow"))
    print(find_LRS_length("aabdbcec"))
    print(find_LRS_length("fmff"))


main()
