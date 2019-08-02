'''
Subset sum
Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.
'''

def has_subset_with_sum(nums, target_sum):
    if sum(nums) < target_sum:
        return False

    memo = {}
    return has_subset_with_sum_recursive(nums, target_sum, 0, memo)


def has_subset_with_sum_recursive(nums, target_sum, index, memo):

    if target_sum == 0:
        return True

    n = len(nums)

    if n == 0 or index >= n:
        return False

    if (target_sum, index) in memo:
        return memo[(target_sum, index)]

    res1 = False
    if nums[index] <= target_sum:
        res1 = has_subset_with_sum_recursive(nums, target_sum-nums[index], index + 1, memo)

    res2 = has_subset_with_sum_recursive(nums, target_sum, index + 1, memo)
    memo[(target_sum, index)] = res1 or res2

    return memo[(target_sum, index)]


print("Can partition: " + str(has_subset_with_sum([1, 2, 3, 7], 10)))
print("Can partition: " + str(has_subset_with_sum([1, 2, 7, 1, 5], 9)))
print("Can partition: " + str(has_subset_with_sum([1, 3, 4, 8], 11)))

