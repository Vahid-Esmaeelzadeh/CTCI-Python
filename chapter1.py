# region Question 1.2
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
# endregion
# region Question 1.3
def URLify(str, n):
    lst = list(str)
    spaces = 0

    for i in range(n):
        if lst[i] == ' ':
            spaces += 1

    index = n + spaces * 2
    for i in range(n-1, -1, -1):
        if lst[i] == ' ':
            lst[index-3:index] = '%20'
            index -= 3
        else:
            lst[index-1] = lst[i]
            index -= 1

    return ''.join(lst)

print(URLify(' Vahid E    ', 8))


# endregion
# region Question 1.4
def PalinPermutatoin(str):
    letters = [False] * 128

    for c in str:
        if c != ' ':
            letters[ord(c.lower())] ^= True

    odd_letters_count = 0

    for b in letters:
        if b is True:
            odd_letters_count += 1
        if odd_letters_count > 1:
            return False

    return True

def PalinPermutatoin_bit(str):

    letters = 0
    for c in str:
        if c != ' ':
            index = 1 << ord(c.lower()) - ord('a')
            letters ^= index

    if letters == 0:
        return True
    if (letters - 1) & letters == 0:
        return True

    return False

print(PalinPermutatoin('Vahid vhdidd'))

print(PalinPermutatoin_bit('vahid dihav'))
# endregion
# region Question 1.5
def oneAway(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    i = 0
    j = 0
    dif = 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
            j += 1
        elif str1[i+1] == str2[j]:
            dif += 1
            i += 1
        elif str1[i] == str2[j+1]:
            dif += 1
            j += 1
        else:
            i += 1
            j += 1
            dif += 1

    if dif + len(str1) - i + len(str2) - j > 1:
        return False
    return True

print(oneAway('pale', 'bake'))
# endregion
# region Question 1.6
def StringCompression1(s):
    res = ''
    letters = [0] * 58 # index of all letters (A-Z, a-z)
    for c in s:
        letters[ord(c) - ord('A')] += 1

    for i in range(len(letters)):
        if len(res) > len(s):
            return s
        if letters[i] > 0:
            res = res + chr(i+ord('A')) + str(letters[i])

    return res
def StringCompression2(s):
    if countCompression(s) >= len(s):
        return s

    compressed = ""
    count_consecutive = 0

    for i in range(len(s)):
        count_consecutive += 1
        if i + 1 >= len(s) or s[i] != s[i+1]:
            compressed = compressed + s[i] + str(count_consecutive)
            count_consecutive = 0

    return compressed
def countCompression(s):
    comp_len = 0
    consecutive_len = 0

    for i in range(len(s)):
        consecutive_len += 1
        if i + 1 >= len(s) or s[i] != s[i+1]:
            comp_len += 1 + len(str(consecutive_len))
            consecutive_len = 0

    return comp_len

print(StringCompression2('ttttta   abccccc'))
# endregion
# region Question 1.7
import math

def rotateMatrix(mat):
    n = len(mat)
    for i in range(math.ceil(n/2)):
        for j in range(i, n-i-1, 1):
            tmp = mat[i][j]
            mat[i][j] = mat[n-j-1][i]
            mat[n-j-1][i] = mat[n-i-1][n-j-1]
            mat[n-i-1][n-j-1] = mat[j][n-i-1]
            mat[j][n-i-1] = tmp


mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for r in mat:
    for c in r:
        print(c, end=" ")
    print()

rotateMatrix(mat)
print(mat)
for r in mat:
    for c in r:
        print(c, end=" ")
    print()
# endregion
# region Question 1.8
from numpy import *

def zeroMatrix1(A): # O(MN) space complexity
    mask = ones(shape(A))
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 0:
                mask[i, :] = 0
                mask[:, j] = 0

    for i in range(len(mask)):
        for j in range(len(mask[0])):
            if mask[i][j] == 0:
                A[i][j] = 0

def zeroMatrix2(A: array): # O(1) space complexity

    m = len(A)
    n = 0
    if m > 0:
        n = len(A[0])

    first_row_has_zero = ~all(A[0])
    first_col_has_zero = ~all(A[:, 0])

    #[i for (i, row) in enumerate(A) if not all(row)]
    for i in range(1, m):
        for j in range(1, n):
            if A[i, j] == 0:
                A[i][0] = 0
                A[0][j] = 0

    for i in range(1, m):
        if A[i][0] == 0:
            A[i, :] = [0]*n

    for j in range(1, n):
        if A[0][j] == 0:
            A[:, j] = transpose([0]*m)

    if first_row_has_zero:
        A[0, :] = [0]*n
    if first_col_has_zero:
        A[:, 0] = transpose([0]*m)

mat = array([[1, 2, 3, 4], [2, 0, -2, 1], [2, 2, 2, 2]])

print(mat)
zeroMatrix1(mat)
print(mat)

A = array([[1, 1, 3, 4], [2, 1, 0, 1], [2, 2, 2, 2]])
zeroMatrix2(A)
print(A)
# endregion
# region Question 1.9
def stringRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) == 0:
        return True

    index = s1.find(s2[:int(len(s2)/2)])

    s1 = s1[index:] + s1[:index]
    if s1 == s2:
        return True
    return False

s1 = "waterbottle"
s2 = "erbottlewat"

print(s1.find("ah"))
print(s2[:int(len(s2)/2)])
print(stringRotation(s1,s2))
# endregion
