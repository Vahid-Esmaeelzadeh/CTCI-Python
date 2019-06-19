from typing import List

# region Question 8.7 (permutations)
def permutations(s: str) -> List[str]:
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


strList = '\n'.join(permutations("aab"))
print(strList)

#endregion
