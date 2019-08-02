'''
String Rotation: Assumeyou have a method i5Sub 5tring which checks if one word is a substring
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
call to i5Sub5tring (e.g.,"waterbottle" is a rotation of"erbottlewat").
'''


def isRotation(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    return s1 in s2 + s2

s1 = "Vahid"
s2 = "ahidV"
print(isRotation(s2, s1))
