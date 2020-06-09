# Contiguous Array
# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
#
# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.


def findMaxLength(nums) -> int:
    zero_count = 0
    for x in nums:
        if x == 0:
            zero_count += 1
    return helper(nums, 0, len(nums) - 1, zero_count, {})


def helper(nums, i, j, zero_count, memo):
    if i > j:
        return 0

    if j - i + 1 == 2 * zero_count:
        return j - i + 1

    if (i, j, zero_count) in memo:
        return memo[(i, j, zero_count)]

    l1 = helper(nums, i+1, j, zero_count - 1 if nums[i] == 0 else zero_count, memo)
    l2 = helper(nums, i, j-1, zero_count - 1 if nums[j] == 0 else zero_count, memo)

    memo[(i, j, zero_count)] = max(l1, l2)
    return memo[(i, j, zero_count)]


a = [0,1,1,1,1,0,1,0,0,0]
print(findMaxLength(a))

