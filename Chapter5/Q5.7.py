def pairWiseSwap(n: int):
    evenBits = n & 0x5555_5555
    oddBits = n & 0xAAAA_AAAA

    return (evenBits << 1) | (oddBits >> 1)


a = 138
print(bin(138))
print(bin(pairWiseSwap(a)))
