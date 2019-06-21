def isPalindromePermutaion(s: str) -> bool:
    charTable = dict()
    for c in s:
        if c not in charTable:
            charTable[c] = 0
        charTable[c] += 1

    foundOdd = False
    for c in charTable:
        if charTable[c] % 2 == 1:
            if foundOdd == True:
                return False
            foundOdd = True

    return True

def isPalindromePermutaion2(s: str) -> bool:
    charFlags = 0

    for c in s:
        charFlags ^= (1 << ord(c))

    return (charFlags & (charFlags - 1)) == 0


print(isPalindromePermutaion("VahidiVd"))
print(isPalindromePermutaion("VahidiVd"))