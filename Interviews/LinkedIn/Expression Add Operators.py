'''
Expression Add Operators

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary
operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
'''


def addOperators1(num, target):
    def dfs(l, r, expr, cur, last, res):
        if l == r:
            if cur == target:
                res.append(expr)
            return
        for i in range(l + 1, r + 1):
            if i == l + 1 or (i > l + 1 and num[l] != "0"):  # prevent "00"
                s, x = num[l:i], int(num[l:i])
                if last == None:
                    dfs(i, r, s, x, x, res)
                else:
                    dfs(i, r, expr + "+" + s, cur + x, x, res)
                    dfs(i, r, expr + "-" + s, cur - x, -x, res)
                    dfs(i, r, expr + "*" + s, cur - last + last * x, last * x, res)

    res = []
    dfs(0, len(num), '', 0, None, res)
    return res


def addOperators(num, target):
    answers = []
    recurse(num, target, 0, 0, 0, 0, [], answers)
    return answers


def recurse(num, target, index, prev_operand, current_operand, value, string, answers):
    # Done processing all the digits in num
    if index == len(num):

        # If the final value == target expected AND
        # no operand is left unprocessed
        if value == target and current_operand == 0:
            answers.append("".join(string[1:]))
        return

    # Extending the current operand by one digit
    current_operand = current_operand * 10 + int(num[index])
    str_op = str(current_operand)

    # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
    # valid operand. Hence this check
    if current_operand > 0:
        # NO OP recursion
        recurse(num, target, index + 1, prev_operand, current_operand, value, string, answers)

    # ADDITION
    string.append('+')
    string.append(str_op)
    recurse(num, target, index + 1, current_operand, 0, value + current_operand, string, answers)
    string.pop()
    string.pop()

    # Can subtract or multiply only if there are some previous operands
    if string:
        # SUBTRACTION
        string.append('-')
        string.append(str_op)
        recurse(num, target, index + 1, -current_operand, 0, value - current_operand, string, answers)
        string.pop()
        string.pop()

        # MULTIPLICATION
        string.append('*')
        string.append(str_op)
        recurse(num, target, index + 1, current_operand * prev_operand, 0,
                value - prev_operand + (current_operand * prev_operand), string, answers)
        string.pop()
        string.pop()

num = "232"
target = 8

print(addOperators1(num, target))