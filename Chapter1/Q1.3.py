'''
URLify: Write a method to replace all spaces in a string with '%20' You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: if implementing in Java, please use a character array so that you can
perform this operation in place.)

EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
'''


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

str1 = "Dr Vahid Esmaeelzadeh    ";
str2 = replaceSpaces(str1, 21)
print(str2)
