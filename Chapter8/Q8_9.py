'''
Parens: Implement an algorithm to print all valid (i.e., properly opened and closed) combinations
of n pairs of parentheses.

EXAMPLE

Input: 3
Output: ((()) ) , (()()) , (())(), ()(()) , () () ()

'''


# region basic recursive solution
def parens1(n):
    if n == 1:
        return ['()']

    lst = parens1(n-1)
    result = []
    for s in lst:
        # at the beginning
        newString = '()' + s
        if newString not in result:
            result.append(newString)
        # after each '('
        for j in range(len(s)):
            if s[j] == '(':
                newString = s[:j+1] + '()' + s[j+1:]
                if newString not in result:
                    result.append(newString)

    return result
# endregion


# region optimal recursive solution
# refer to Educative/Subsets/balanced_parentheses.py
# endregion


print("\n".join(parens1(4)))



