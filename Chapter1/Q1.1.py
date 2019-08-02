'''
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
'''


def is_unique(s: str):
    if len(s) > 128:
        return False

    buffer = [False] * 128
    for c in s:
        if buffer[ord(c)] is True:
            return False
        else:
            buffer[ord(c)] = True
    return True


def is_unique2(s: str):
    buffer = 0
    for c in s:
        code = ord(c)
        if (1 << code) & buffer != 0:
            return False
        buffer |= (1 << code)

    return True


print(is_unique("a$b$%&#*"))
print(is_unique2("ab#$%^&"))

