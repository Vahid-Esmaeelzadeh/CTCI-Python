'''
Minimum Subset Sum Difference
Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.
'''


def minimum_subset_sum_difference(nums):
    #sum2 = sum(nums)
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


print(minimum_subset_sum_difference([1, 2, 3, 9]))
print(minimum_subset_sum_difference([1, 2, 7, 1, 5]))
print(minimum_subset_sum_difference([1, 3, 100, 4]))
