'''
Evaluate Expression

Given an expression containing digits and operations (+, -, *), find all possible ways in which the expression can be
evaluated by grouping the numbers and operators using parentheses.
'''


def diff_ways_to_evaluate_expression(expr):
    if len(expr) == 1:
        return [int(expr)]

    result = []
    for i in range(1, len(expr), 2):
        operator = expr[i]
        operand1 = expr[0:i]
        operand2 = expr[i+1:]
        res1 = diff_ways_to_evaluate_expression(operand1)  # res1 will be a list of integers
        res2 = diff_ways_to_evaluate_expression(operand2)  # res2 will be a list of integers

        for x in res1:
            for y in res2:
                if operator == "+":
                    result.append(x + y)
                elif operator == "-":
                    result.append(x - y)
                elif operator == "*":
                    result.append(x * y)
    return result

def diff_ways_to_evaluate_expression_dp(expr):
    memo = {}
    return diff_ways_to_evaluate_expression_memo(expr, memo)

def diff_ways_to_evaluate_expression_memo(expr, memo):
    if len(expr) == 1:
        return [int(expr)]

    if expr in memo:
        return memo[expr]

    result = []
    for i in range(1, len(expr), 2):
        operator = expr[i]
        operand1 = expr[0:i]
        operand2 = expr[i+1:]
        res1 = diff_ways_to_evaluate_expression(operand1)  # res1 will be a list of integers
        res2 = diff_ways_to_evaluate_expression(operand2)  # res2 will be a list of integers

        for x in res1:
            for y in res2:
                if operator == "+":
                    result.append(x + y)
                elif operator == "-":
                    result.append(x - y)
                elif operator == "*":
                    result.append(x * y)

    memo[expr] = result
    return result


def main():
    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression_dp("1+2*3")))

    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression_dp("2*3-4-5")))


main()
