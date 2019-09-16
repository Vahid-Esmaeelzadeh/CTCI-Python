'''
Count of Palindromic Substrings
'''


def count_PS(st):
    return helper(st, 0)


def helper(st, index):
    if index == len(st) - 1:
        return 1

    count = helper(st, index + 1)
    if st[index] == st[-1]:
        count += 1

    return count + 1


print(count_PS("abdbca"))
print(count_PS("cddpd"))
print(count_PS("pqr"))
print(count_PS("aaaa"))
