'''
Flip Bit to Win: You have an integer and you can flip exactly one bit from a O to a 1. Write code to
find the length of the longest sequence of 1s you could create.

EXAMPLE
Input: 1775 (or: 11011101111)
Output: 8
'''


def flipBitToWin(N: int) -> int:
    count = 1
    newZeroIndex = -1
    midZeroIndex = None
    oldZeroIndex = None
    i = 0

    while N > 0:
        if (1 & N) == 0:
            oldZeroIndex = midZeroIndex
            midZeroIndex = newZeroIndex
            newZeroIndex = i

            if (newZeroIndex is not None) and (oldZeroIndex is not None):
                count = max(count, newZeroIndex - oldZeroIndex - 1)

        i += 1
        N = N >> 1

    oldZeroIndex = midZeroIndex
    newZeroIndex = i

    if newZeroIndex is not None and oldZeroIndex is not None:
        count = max(count, newZeroIndex - oldZeroIndex - 1)

    return count

num = 0xFFFF_FFFF_FFF7
print(bin(num))
print(flipBitToWin(num))

