def getBit(num: int, i: int) -> int:
    return int((num & (1 << i)) != 0)

def setBit(num: int, i: int) -> int:
    return num | (1 << i)

def clearBit(num: int, i: int) -> int:
    mask = ~(1 << i)
    return num & mask

def updateBit1(num: int, i: int, val: bool) -> int:
    if val:
        return setBit(num, i)
    else:
        return clearBit(num, i)

def updateBit(num: int, i: int, val: bool) -> int:
    mask = ~(1 << i)
    return (num & mask) | (int(val) << i)

def clearBitsMSBthroughI(num: int, i: int) -> int:
    mask = (1 << i) - 1
    return num & mask
def clearBitsIthrough0(num: int, i: int) -> int:
    mask = (-1 << (i + 1))
    return num & mask


print(getBit(25,0))
print(setBit(25, 2))
print(updateBit(25, 0, False))
print(clearBit(25, 0))
print(updateBit(25, 2, True))


