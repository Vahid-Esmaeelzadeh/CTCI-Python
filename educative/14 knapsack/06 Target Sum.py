'''
Target Sum

You are given a set of positive numbers and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign.
We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’.


Example 1:
Input: {1, 1, 2, 3}, S=1
Output: 3
Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}
'''


def targetSum(arr, S):
    if len(arr) == 0:
        return 0
    memo = {}
    return helper(arr, S, 0, memo)


def helper(arr, S, index, memo):
    if index == len(arr):
        if S == 0:
            return 1
        return 0

    if (S, index) not in memo:
        count1 = helper(arr, S - arr[index], index + 1, memo)
        count2 = helper(arr, S + arr[index], index + 1, memo)

        memo[(S, index)] = count1 + count2

    return memo[(S, index)]

# Also, we can convert this problem to the problem 5 as follows:
# Find the count of subsets of the given numbers whose sum is equal to (S + Sum(nums)) / 2


def target_sum(nums, s):
    total_sum = sum(nums)
    if total_sum < s or (s + total_sum) % 2 == 1:
        return 0
    return count_subsets_tabulation(nums, (s + sum(nums)) // 2)


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


print(targetSum([1, 1, 2, 3], 1))
print(targetSum([1, 2, 7, 1], 9))

print(target_sum([1, 1, 2, 3], 1))
print(target_sum([1, 2, 7, 1], 9))
