'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
'''


def checkPermutation(s1: str, s2: str):
    if len(s1) != len(s2):
        return False

    charCount = [0] * 128

    for c in s1:
        charCount[ord(c)] += 1

    for c in s2:
        charCount[ord(c)] -= 1
        if charCount[ord(c)] < 0:
            return False

    return True

def checkPermutation2(s1: str, s2: str):
    return sorted(s1) == sorted(s2)


str1 = "vahid"
str2 = "dihav"

print(checkPermutation(str1, str2))
print(checkPermutation2(str1, str2))
