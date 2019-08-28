'''
Parens:

For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.
Valid balanced parentheses
'''

from collections import deque


class ParenthesesString:
    def __init__(self, s="", open_count=0, close_count=0):
        self.s = s
        self.open_count = open_count
        self.close_count = close_count


# region iterative solution
def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(ParenthesesString("", 0, 0))
    while queue:
        ps = queue.popleft()
        # if we've reached the maximum number of open and close parentheses, add to the result
        if ps.open_count == num and ps.close_count == num:
            result.append(ps.s)
        else:
            if ps.open_count < num:  # if we can add an open parentheses, add it
                queue.append(ParenthesesString(ps.s + "(", ps.open_count + 1, ps.close_count))

            if ps.open_count > ps.close_count:  # if we can add a close parentheses, add it
                queue.append(ParenthesesString(ps.s + ")", ps.open_count, ps.close_count + 1))

    return result


# endregion


# region recursive solution
def generate_valid_parentheses2(num):
    result = []
    parenthesesString = [0 for x in range(2 * num)]
    generate_valid_parentheses_rec(num, 0, 0, parenthesesString, 0, result)
    return result


def generate_valid_parentheses_rec(num, openCount, closeCount, parenthesesString, index, result):
    # if we've reached the maximum number of open and close parentheses, add to the result
    if openCount == num and closeCount == num:
        result.append(''.join(parenthesesString))
    else:
        if openCount < num:  # if we can add an open parentheses, add it
            parenthesesString[index] = '('
            generate_valid_parentheses_rec(num, openCount + 1, closeCount, parenthesesString, index + 1, result)

        if openCount > closeCount:  # if we can add a close parentheses, add it
            parenthesesString[index] = ')'
            generate_valid_parentheses_rec(num, openCount, closeCount + 1, parenthesesString, index + 1, result)

# endregion


print(generate_valid_parentheses(2))
print(generate_valid_parentheses(3))
print(generate_valid_parentheses(4))
print(generate_valid_parentheses2(4))

# FINAL REVIEW NEEDED
