'''
valid parentheses
'''


def areParanthesisBalanced(expr):
    s = []
    parentheses = {'(', ')', '[', ']', '{', '}'}

    for i in range(len(expr)):
        if expr[i] not in parentheses:
            continue

        if expr[i] == '(' or expr[i] == '[' or expr[i] == '{':
            s.append(expr[i])
            continue

        if len(s) == 0:  # it is a right paren, and we don't have any left before
            return False

        if expr[i] == ')':
            x = s.pop()
            if x == '{' or x == '[':
                return False

        elif expr[i] == '}':
            x = s.pop()
            if x == '(' or x == '[':
                return False

        elif expr[i] == ']':
            x = s.pop()
            if x == '(' or x == '{':
                return False

    if len(s) == 0:
        return True
    return False



expr = "{aaa}{(s)fs}[ab]";
print(areParanthesisBalanced(expr))
