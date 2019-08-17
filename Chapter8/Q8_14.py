'''
Boolean Evaluation: Given a boolean expression consisting of the symbols 0 (false), 1 (true), &
(AND), I (OR), and /\ (XOR), and a desired boolean result value result, implement a function to
count the number of ways of parenthesizing the expression such that it evaluates to result. The
expression should be fully parenthesized (e.g., ( 0)A( 1)) but not extraneously (e.g., ( ( ( 0))/\( 1))).

EXAMPLE
countEval("l^0|0|1", false) -> 2
countEval("0&0&0&1^l|0", true)-> 10

Idea:
0&0&0&1^l|0
possible ways to do the first step:

(0)&(0&0&1^l|0)
(0&0)&(0&1^l|0)
(0&0&0)&(1^l|0)
(0&0&0&1)^(l|0)
(0&0&0&1^l)|(0)

'''


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

        if result is True:
            ways += totalTrue
        else:
            ways += total - totalTrue

    memo[(expr, result)] = ways
    return ways


print(boolEval("1^0&0&0&1^1|0&1|0", False))


