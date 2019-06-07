def stringRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) == 0:
        return True

    index = s1.find(s2[:int(len(s2)/2)])

    s1 = s1[index:] + s1[:index]
    if s1 == s2:
        return True
    return False

s1 = "waterbottle"
s2 = "erbottlewat"

print(s1.find("ah"))
print(s2[:int(len(s2)/2)])
print(stringRotation(s1,s2))
