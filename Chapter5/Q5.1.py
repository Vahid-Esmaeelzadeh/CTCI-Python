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