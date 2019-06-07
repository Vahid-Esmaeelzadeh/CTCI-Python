from itertools import permutations

# using permutation
def check_permutation(str1, str2):

    if len(str1) != len(str2):
        return False

    perm1 = list(permutations(str1))
    return tuple(str2) in perm1

# using sort
def check_permutation_sort(str1, str2):

    if len(str1) != len(str2):
        return False

    if sorted(str1) == sorted(str2):
        return True
    return False

# count identical characters
def check_permutation_count(str1, str2):

    #if len(str1) != len(str2):
    #    return False

    letters = [0] * 128
    for i in range(len(str1)):
        if str1[i] != ' ':
            letters[ord(str1[i])] += 1

    for i in range(len(str2)):
        if str2[i] != ' ':
            letters[ord(str2[i])] -= 1
            if letters[ord(str2[i])] < 0:
                return False

    return True

print(check_permutation('abc', 'cba'))
print(check_permutation_sort('Vahid', 'vahid'))
print(check_permutation_count(' abc   daa', 'aa      cbda'))
