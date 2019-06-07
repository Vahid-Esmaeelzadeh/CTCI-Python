# region Question 8.7 (permutations)
def permutations(str):
    if len(str) == 0:
        return ['']

    prevList = permutations(str[1:])
    nextList = []

    for i in range(len(prevList)):
        for j in range(len(str)):
            newString = prevList[i][:j] + str[0] + prevList[i][j:]
            if newString not in nextList:
                nextList.append(newString)

    return nextList

strList = '\n'.join(permutations('aaab'))
print(strList)


#endregion
