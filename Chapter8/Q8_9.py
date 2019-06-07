# region Question 8.9 (parens)
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

print('\n'.join(parens1(4)))

# endregion
