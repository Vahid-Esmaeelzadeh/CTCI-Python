# region Question 8.1 (countWays)
def countways1(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    return countways1(n-1) + countways1(n-2) + countways1(n-3)

def countways2(n: int) -> int:
    memo = [None] * (n+1)
    return countways2_helper(n, memo)

def countways2_helper(n: int, memo: list):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if memo[n] is None:
        memo[n] = countways2_helper(n-1, memo) + countways2_helper(n-2, memo) + countways2_helper(n-3, memo)
    return memo[n]

def countways3(n: int):
    if n < 0:
        return 0
    if n == 1 or n == 0:
        return 1
    if n == 2:
        return 2

    c0 = 1
    c1 = 1
    c2 = 2
    count = 0

    for i in range(3, n+1):
        count = c0 + c1 + c2
        c0 = c1
        c1 = c2
        c2 = count

    return count

print(countways1(10))
print(countways2(10))
print(countways3(10))
# endregion
