def isUnique(s: str):
    buffer = [False] * 128
    for c in s:
        if buffer[ord(c)] == True :
            return False
        else:
            buffer[ord(c)] = True
    return True

def isUnique2(s: str):
    buffer: int = 0
    for c in s:
        code = ord(c)
        if (1 << code) & buffer != 0:
            return False
        buffer |= (1 << code)

    return True

print(isUnique("a$b$%&#*"))
print(isUnique2("ab#$%^&"))

