'''
is number
'''


def isNumber(s: str) -> bool:
    # states
    start = 0
    int_sign = 1
    integer = 2
    point = 3
    frac = 4
    exp = 5
    exp_sign = 6
    exp_int = 7

    # inputs
    digit = 1
    sign = 2
    dot = 3
    e = 4

    def classify(c):
        if c in '0123456789': return digit
        if c == '.': return dot
        if c in '+-': return sign
        if c == 'e': return e
        raise ValueError

    machine = {
        start: {sign: int_sign, digit: integer, dot: point},
        int_sign: {digit: integer, dot: point},
        integer: {digit: integer, dot: frac, e: exp},
        point: {digit: frac},
        frac: {digit: frac, e: exp},
        exp: {digit: exp_int, sign: exp_sign},
        exp_sign: {digit: exp_int},
        exp_int: {digit: exp_int},
    }

    state = start
    for c in s.strip():
        try:
            state = machine[state][classify(c)]
        except:
            return False
    return state in [integer, frac, exp_int]


print(isNumber('-12.34'))

s = "  12.75   "
aa = s.split()
