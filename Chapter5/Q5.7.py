'''
Pairwise Swap: Write a program to swap odd and even bits in an integer with as few instructions as
possible (e.g., bit O and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
'''


def pairWiseSwap(n: int):
    evenBits = n & 0x5555_5555
    oddBits = n & 0xAAAA_AAAA

    return (evenBits << 1) | (oddBits >> 1)


a = 138
print(bin(138))
print(bin(pairWiseSwap(a)))
