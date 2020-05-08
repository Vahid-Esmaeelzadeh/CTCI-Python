'''
Minimum Subset Sum Difference
Given a set of positive numbers, partition the set into two subsets with minimum difference between
their subset sums.
'''
import math


def minimum_subset_sum_difference(nums):
    memo = {}
    return recursive(nums, 0, 0, 0, memo)


def recursive(nums, index, sum1, sum2, memo):
    n = len(nums)

    if index >= n:
        return abs(sum1 - sum2)

    if (index, sum1) in memo:
        return memo[(index, sum1)]

    diff1 = recursive(nums, index + 1, sum1 + nums[index], sum2, memo)
    diff2 = recursive(nums, index + 1, sum1, sum2 + nums[index], memo)

    memo[(index, sum1)] = min(diff1, diff2)

    return min(diff1, diff2)


def can_partition(num):
    s = sum(num)
    dp = [[-1 for x in range(s + 1)] for y in range(len(num))]
    result = can_partition_recursive(dp, num, 0, 0, 0)
    return result


def can_partition_recursive(dp, num, currentIndex, sum1, sum2):
    # base check
    if currentIndex == len(num):
        return abs(sum1 - sum2)
    # check if we have not already processed similar problem
    if dp[currentIndex][sum1] == -1:
        # recursive call after including the number at the currentIndex in the first set
        diff1 = can_partition_recursive(
            dp, num, currentIndex + 1, sum1 + num[currentIndex], sum2)

        # recursive call after including the number at the currentIndex in the second set
        diff2 = can_partition_recursive(
            dp, num, currentIndex + 1, sum1, sum2 + num[currentIndex])

        dp[currentIndex][sum1] = min(diff1, diff2)

    return dp[currentIndex][sum1]


def minimum_subset_sum_difference_tabulation(nums):
    # matrix size: [0:n]x[0:sum]
    n = len(nums)
    total_sum = sum(nums)

    dp = [[-1 for _ in range(total_sum + 1)] for _ in range(n + 1)]
    for sum1 in range(total_sum + 1):
        sum2 = total_sum - sum1
        dp[n][sum1] = abs(sum1 - sum2)

    for i in range(n - 1, -1, -1):
        s = 0
        while s + nums[i] <= total_sum:
            diff1 = dp[i + 1][nums[i] + s]
            diff2 = dp[i + 1][s]
            dp[i][s] = min(diff1, diff2)
            s += 1
    return dp[0][0]


print(minimum_subset_sum_difference([1, 2, 3, 9]), end=' ')
print(minimum_subset_sum_difference([1, 20, 7, 1, 5]), end=' ')
print(minimum_subset_sum_difference([1, 3, 200, 4]))

print(can_partition([1, 2, 3, 9]), end=' ')
print(can_partition([1, 20, 7, 1, 5]), end=' ')
print(can_partition([1, 3, 200, 4]))

print(minimum_subset_sum_difference_tabulation([1, 2, 3, 9]), end=' ')
print(minimum_subset_sum_difference_tabulation([1, 20, 7, 1, 5]), end=' ')
print(minimum_subset_sum_difference_tabulation([1, 3, 200, 4]))
