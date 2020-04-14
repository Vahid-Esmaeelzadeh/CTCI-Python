'''
Count of Subset Sum
'''


def count_subsets(num, sum):
    return count_subsets_recursive(num, sum, 0)


def count_subsets_recursive(num, sum, currentIndex):
    # base checks
    if sum == 0:
        return 1
    n = len(num)
    if n == 0 or currentIndex >= n:
        return 0

    # recursive call after selecting the number at the currentIndex
    # if the number at currentIndex exceeds the sum, we shouldn't process this
    sum1 = 0
    if num[currentIndex] <= sum:
        sum1 = count_subsets_recursive(
            num, sum - num[currentIndex], currentIndex + 1)

    # recursive call after excluding the number at the currentIndex
    sum2 = count_subsets_recursive(num, sum, currentIndex + 1)

    return sum1 + sum2


def count_subsets_memo(num, sum):
    dp = [[-1 for x in range(sum + 1)] for y in range(len(num))]
    return count_subsets_recursive_memo(dp, num, sum, 0)


def count_subsets_recursive_memo(dp, num, sum, currentIndex):
    # base checks
    if sum == 0:
        return 1

    n = len(num)
    if n == 0 or currentIndex >= n:
        return 0

    # check if we have not already processed a similar problem
    if dp[currentIndex][sum] == -1:
        # recursive call after choosing the number at the currentIndex
        # if the number at currentIndex exceeds the sum, we shouldn't process this
        sum1 = 0
        if num[currentIndex] <= sum:
            sum1 = count_subsets_recursive_memo(
                dp, num, sum - num[currentIndex], currentIndex + 1)

        # recursive call after excluding the number at the currentIndex
        sum2 = count_subsets_recursive_memo(dp, num, sum, currentIndex + 1)

        dp[currentIndex][sum] = sum1 + sum2

    return dp[currentIndex][sum]


def count_subsets_tabulation(nums, s):
    if s == 0:
        return 1
    n = len(nums)

    dp = [[0 for _ in range(s + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(n - 1, -1, -1):
        for cur_sum in range(1, s + 1):
            sum1, sum2 = 0, 0
            if nums[i] <= cur_sum:
                sum1 = dp[i + 1][cur_sum - nums[i]]
            sum2 = dp[i + 1][cur_sum]
            dp[i][cur_sum] = sum1 + sum2

    return dp[0][-1]


def main():
    print("Total number of subsets " + str(count_subsets([1, 7, 2, 3], 2)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))

    print("Total number of subsets " + str(count_subsets_memo([1, 7, 2, 3], 2)))
    print("Total number of subsets: " + str(count_subsets_memo([1, 2, 7, 1, 5], 9)))

    print("Total number of subsets " + str(count_subsets_tabulation([1, 7, 2, 3], 2)))
    print("Total number of subsets: " + str(count_subsets_tabulation([1, 2, 7, 1, 5], 9)))

main()
