'''
Recursive Multiply: Write a recursive function to multiply two positive integers without using
the * operator (or / operator). You can use addition, subtraction, and bit shifting, but you should
minimize the number of those operations.
'''


# region my solution - O(s)
def recurMul (a, b):
    if a > b:
        return recurMulHelper(a, b, 0)
    else:
        return recurMulHelper(b, a, 0)


def recurMulHelper(a, b, i):
    if b == 0:
        return 0

    temp = 0
    if (b & 1) == 1:
        temp = a

    return (temp << i) + recurMulHelper(a, b >> 1, i+1)
# endregion


# region CTCI solution O(log s)
def minProduct(a, b):
    bigger = a if a > b else b
    smaller = a if a < b else b
    return minProductHelper(smaller, bigger)


def minProductHelper(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger

    s = smaller >> 1
    halfProd = minProductHelper(s, bigger)

    if smaller % 2 == 0:
        return halfProd + halfProd
    else:
        return halfProd + halfProd + bigger
# endregion



print(recurMul(12345679, 72))
print(minProduct(12345679, 63))
