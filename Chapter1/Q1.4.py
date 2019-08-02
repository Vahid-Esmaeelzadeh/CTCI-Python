'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat'; "atco eta·; etc.)
'''


# using bit-vector as a hash-table
def isPalindromePermutaion2(s: str) -> bool:
    charFlags = 0

    for c in s:
        charFlags ^= (1 << ord(c))

    return (charFlags & (charFlags - 1)) == 0


def isPalindromePermutaion(s: str) -> bool:
    charTable = dict()
    for c in s:
        charTable[c] = charTable.get(c, 0) + 1
        # if c not in charTable:
        #     charTable[c] = 0
        # charTable[c] += 1

    foundOdd = False
    for c in charTable:
        if charTable[c] % 2 == 1:
            if foundOdd:
                return False
            foundOdd = True

    return True



print(isPalindromePermutaion("VahidiVd"))
print(isPalindromePermutaion("VahidiVd"))