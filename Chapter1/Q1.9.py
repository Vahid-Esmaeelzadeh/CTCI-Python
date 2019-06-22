def isRotation(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    return s1 in s2 + s2

s1 = "Vahid"
s2 = "ahidV"
print(isRotation(s2, s1))
