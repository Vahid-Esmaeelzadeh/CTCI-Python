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


def target_sum_tabulation(arr, s):
    n = len(arr)
    if n == 0:
        return 0

    min_sum, max_sum = -sum(arr), sum(arr)
    dp = {(n % 2, 0): 1}
    result = 0
    for i in range(n - 1, -1, -1):
        for cur_sum in range(min_sum, max_sum + 1):
            count1 = dp.get(((i + 1) % 2, cur_sum - arr[i]), 0)
            count2 = dp.get(((i + 1) % 2, cur_sum + arr[i]), 0)

            dp[(i % 2, cur_sum)] = count1 + count2
            if i == 0:
                result = max(result, count1 + count2)
    return result


print(targetSum([1, 1, 2, 3], 1))
print(targetSum([1, 2, 7, 1], 9))

print(target_sum_tabulation([1, 1, 2, 3], 1))
print(target_sum_tabulation([1, 2, 7, 1], 9))
