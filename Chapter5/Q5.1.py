'''
Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method
to insert M into N such that M starts at bit j and ends at bit i. You can assume that the bits j through
ihave enough space to fit all of M. That is, if M = 10011, you can assume that there are at least 5
bits between j and i. You would not, for example, have j = 3 and i= 2, because M could not fully
fit between bit 3 and bit 2.

EXAMPLE
Input: N
Output: N
SOLUTION
10000000000, M
10001001100
'''

from Chapter5.basicOperations import *

def insertion(N: int, M: int, j: int, i: int):
    mask1 = (1 << i) - 1
    mask2 = (-1 << (j + 1))
    mask = mask1 | mask2

    # clear the bits from j through i
    N = N & mask
    # update the bits from j through i
    N = N | (M << i)

    return N


N = insertion(0xFFFF, 0xA, 9, 5)
print(bin(0xffff))
print(bin(N))