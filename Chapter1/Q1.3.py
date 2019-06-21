def replaceSpaces(s: str, strLen: int):
    lst = list(s)
    spaceCount = lst[:strLen].count(' ')
    endIndex = strLen + spaceCount * 2

    for i in range(strLen - 1, -1, -1):
        if lst[i] != ' ':
            lst[endIndex - 1] = lst[i]
            endIndex -= 1
        else:
            lst[endIndex - 3: endIndex] = "%20"
            endIndex -= 3

    return ''.join(lst)

str1 = "Mr Vahid Esmaeelzadeh    ";
str2 = replaceSpaces(str1, 21)
print(str2)
