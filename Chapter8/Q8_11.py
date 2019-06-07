# region Question 8.11 (coins)
def coins(n):
    if n <= 0:
        return 0
    return coinsHelper(n)

def coinsHelper(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return coinsHelper(n - 1) + coinsHelper(n - 5) + coinsHelper(n - 10) + coinsHelper(n - 25)


def count(S, m, n):
    # If n is 0 then there is 1
    # solution (do not include any coin)
    if (n == 0):
        return 1

    # If n is less than 0 then no
    # solution exists
    if (n < 0):
        return 0;

    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if (m <= 0 and n >= 1):
        return 0

    # count is sum of solutions
    # (i) excluding S[m-1] (ii) including S[m-1]
    return count(S, m - 1, n) + count(S, m, n - S[m - 1]);

def count_DP(S, m, n, memo):
    # If n is 0 then there is 1
    # solution (do not include any coin)
    if (n == 0):
        return 1

    # If n is less than 0 then no
    # solution exists
    if (n < 0):
        return 0;

    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if (m <= 0 and n >= 1):
        return 0

    if (m-1, n) not in memo:
        memo[(m-1, n)] = count_DP(S, m - 1, n, memo)

    if (m, n-S[m-1]) not in memo:
        memo[(m, n-S[m-1])] = count_DP(S, m, n - S[m - 1], memo)
    # count is sum of solutions
    # (i) excluding S[m-1] (ii) including S[m-1]
    return memo[(m-1, n)] + memo[(m, n-S[m-1])]


arr = [25, 10, 5, 1]
m = len(arr)
n = 120
memo = dict()
print(count(arr, m, n))
print(count_DP(arr, m, n, memo))
# endregion
