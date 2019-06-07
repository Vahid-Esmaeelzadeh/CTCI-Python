#region Question 8.5 (recursive multiply)


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


print(recurMul(11,17))
#endregion
