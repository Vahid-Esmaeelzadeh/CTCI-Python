def oneAway(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    i = 0
    j = 0
    dif = 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
            j += 1
        elif str1[i+1] == str2[j]:
            dif += 1
            i += 1
        elif str1[i] == str2[j+1]:
            dif += 1
            j += 1
        else:
            i += 1
            j += 1
            dif += 1

    if dif + len(str1) - i + len(str2) - j > 1:
        return False
    return True

print(oneAway('pale', 'bake'))
