'''
Minimum Coin Change

Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the minimum number
of coins needed to make up that amount.
'''

import math


# my solution
def minCoinChange(den, total):
    res = helper(den, total, 0, 0)
    return res if res != math.inf else -1


def helper(den, total, index, coinsNum):
    if total == 0:
        return coinsNum
    if index >= len(den):
        return math.inf

    count1 = math.inf
    if den[index] <= total:
        count1 = helper(den, total - den[index], index, coinsNum + 1)
    count2 = helper(den, total, index + 1, coinsNum)

    return min(count1, count2)


# educative solution
def count_change(denominations, total):
    result = count_change_recursive(denominations, total, 0)
    return -1 if result == math.inf else result


def count_change_recursive(denominations, total, currentIndex):
    # base check
    if total == 0:
        return 0

    n = len(denominations)
    if n == 0 or currentIndex >= n:
        return math.inf

    # recursive call after selecting the coin at the currentIndex
    # if the coin at currentIndex exceeds the total, we shouldn't process this
    count1 = math.inf
    if denominations[currentIndex] <= total:
        res = count_change_recursive(denominations, total - denominations[currentIndex], currentIndex)
        if res != math.inf:
            count1 = res + 1

    # recursive call after excluding the coin at the currentIndex
    count2 = count_change_recursive(denominations, total, currentIndex + 1)

    return min(count1, count2)


def count_change_tabulation(den, total):
    n = len(den)
    dp = [[math.inf for _ in range(total + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(n - 1, -1, -1):
        for j in range(1,total + 1):
            count1 = math.inf
            if den[i] <= j:
                if dp[i][j - den[i]] != math.inf:
                   count1 = dp[i][j - den[i]] + 1
            count2 = dp[i+1][j]
            dp[i][j] = min(count1, count2)

    return dp[0][total]


def count_change_tabulation_optimal(den, total):
    n = len(den)
    dp0 = [math.inf for _ in range(total + 1)]
    dp1 = [math.inf for _ in range(total + 1)]

    dp0[0] = dp1[0] = 0

    for den_index in range(len(den) - 1, -1, -1):
        for j in range(1, total + 1):
            count1 = math.inf
            if den[den_index] <= j:
                if dp0[j - den[den_index]] != math.inf:
                    count1 = dp0[j - den[den_index]] + 1
            count2 = dp1[j]
            dp0[j] = min(count1, count2)

        dp1[:] = dp0[:]
        dp0 = [0] + [math.inf for _ in range(total)]

    return min(dp0[total], dp1[total])


print(minCoinChange([1, 2, 3], 5))
print(minCoinChange([1, 2, 3], 11))
print(minCoinChange([1, 2, 3], 7))
print(minCoinChange([3, 5], 7))

print(count_change_tabulation([1, 2, 3], 5))
print(count_change_tabulation([1, 2, 3], 11))
print(count_change_tabulation([1, 2, 3], 7))
print(count_change_tabulation([3, 5], 7))


print(count_change_tabulation_optimal([1, 2, 3], 5))
print(count_change_tabulation_optimal([1, 2, 3], 11))
print(count_change_tabulation_optimal([1, 2, 3], 7))
print(count_change_tabulation_optimal([3, 5], 7))
