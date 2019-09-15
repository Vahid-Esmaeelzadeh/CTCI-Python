'''
String Permutations without Dups: [recursive approach]
Write a method to compute all permutations of a string of unique characters.
'''


def permutations(s):
    if len(s) == 0:
        return [""]

    subPerm = permutations(s[1:])
    result = []

    for x in subPerm:
        for i in range(len(s)):
            newString = x[:i] + s[0] + x[i:]
            if newString not in result:
                result.append(newString)

    return result


strList = '\n'.join(permutations("abc"))
print(strList)

