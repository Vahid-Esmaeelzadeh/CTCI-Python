'''
Root of Number
'''


def root(x, n):
    if x == 0:
        return 0

    upper = max(1, x)
    lower = 0
    res = (upper + lower) / 2

    while res - lower >= 0.001:
        if res ** n > x:
            upper = res
        elif res ** n < x:
            lower = res
        else:
            break

        res = (upper + lower) / 2

    return res


print(root(3, 2))
