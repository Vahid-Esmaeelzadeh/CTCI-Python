'''
Coin Change
'''


def count_change(denominations, total):
    return count_change_recursive(denominations, total, 0)


def count_change_recursive(denominations, total, currentIndex):
    # base checks
    if total == 0:
        return 1

    n = len(denominations)
    if n == 0 or currentIndex >= n:
        return 0

    # recursive call after selecting the coin at the currentIndex
    # if the coin at currentIndex exceeds the total, we shouldn't process this
    sum1 = 0
    if denominations[currentIndex] <= total:
        sum1 = count_change_recursive(
            denominations, total - denominations[currentIndex], currentIndex)

    # recursive call after excluding the coin at the currentIndex
    sum2 = count_change_recursive(denominations, total, currentIndex + 1)

    return sum1 + sum2


def count_change_dp(denominations, total):
    dp = [[-1 for _ in range(total + 1)] for _ in range(len(denominations))]
    return count_change_recursive_dp(dp, denominations, total, 0)


def count_change_recursive_dp(dp, denominations, total, currentIndex):
    # base checks
    if total == 0:
        return 1

    n = len(denominations)
    if n == 0 or currentIndex >= n:
        return 0

    if dp[currentIndex][total] != -1:
        return dp[currentIndex][total]

    # recursive call after selecting the coin at the currentIndex
    # if the coin at currentIndex exceeds the total, we shouldn't process this
    sum1 = 0
    if denominations[currentIndex] <= total:
        sum1 = count_change_recursive_dp(
            dp, denominations, total - denominations[currentIndex], currentIndex)

    # recursive call after excluding the coin at the currentIndex
    sum2 = count_change_recursive_dp(dp, denominations, total, currentIndex + 1)

    dp[currentIndex][total] = sum1 + sum2
    return dp[currentIndex][total]


def main():
    print(count_change([1, 2, 3], 5))
    print(count_change_dp([1, 2, 3], 5))


main()
