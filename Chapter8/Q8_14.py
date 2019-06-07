# region Question 8.14 (Boolean Evaulation)


def boolEval(expr: str, result: bool) -> int:
    if len(expr) == 0:
        return 0
    if len(expr) == 1:
        return int(int(expr[0]) == int(result))

    ways = 0
    memo = dict()

    if (expr, result) in memo:
        return memo[(expr, result)]

    for i in range(1, len(expr), 2):
        leftTrue = boolEval(expr[:i], True)
        leftFalse = boolEval(expr[:i], False)
        rightTrue = boolEval(expr[i + 1:], True)
        rightFalse = boolEval(expr[i + 1:], False)

        total = (leftTrue + leftFalse) * (rightTrue + rightFalse)

        totalTrue = 0

        if expr[i] == '^':
            totalTrue = (leftTrue * rightFalse) + (leftFalse * rightTrue)
        elif expr[i] == '&':
            totalTrue = leftTrue * rightTrue
        elif expr[i] == '|':
            totalTrue = (leftTrue * rightTrue) + (leftFalse * rightTrue) + (leftTrue * rightFalse)

        if result:
            ways += totalTrue
        else:
            ways += total - totalTrue

    memo[(expr, result)] = ways
    return ways

print(boolEval("1^0&0&0&1^1|0&1|0", False))
# endregion