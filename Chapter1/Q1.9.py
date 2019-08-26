'''
String Rotation: Assume you have a method is_sub_string which checks if one word is a substring
of another. Given two strings, S1 and S2, write code to check if S2 is a rotation of S1 using only one
call to is_sub_string (e.g.,"waterbottle" is a rotation of"erbottlewat").
'''


def isRotation(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    return s1 in s2 + s2

s1 = "Vahid"
s2 = "ahidV"
print(isRotation(s2, s1))
