'''
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.
'''


def countways1(n: int) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    return countways1(n-1) + countways1(n-2) + countways1(n-3)

def countways2(n: int) -> int:
    memo = [None for _ in range(n + 1)]
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

    # c0, c1, c2, count
    #	   |   |   |
    #	  \/  \/   \/
    # 	  c0, c1, c2

    # c0 <- c1 <- c2 <- count

    for i in range(3, n+1):
        count = c0 + c1 + c2
        c0 = c1
        c1 = c2
        c2 = count

    return count

print(countways1(10))
print(countways2(10))
print(countways3(10))

