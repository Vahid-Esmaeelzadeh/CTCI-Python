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


def mul(a, b):
    if a > b:
        return mul_recursive(a, b, 0)
    else:
        return mul_recursive(b, a, 0)

def mul_recursive(a, b, i): # b is the smaller number
    if b == 0:
        return 0

    if 1 & b == 1:
        return (a << i) + mul_recursive(a, b >> 1, i + 1)
    else:
        return mul_recursive(a, b >> 1, i + 1)



print(recurMul(12345679, 72))
print(mul(12345679, 45))
#endregion
