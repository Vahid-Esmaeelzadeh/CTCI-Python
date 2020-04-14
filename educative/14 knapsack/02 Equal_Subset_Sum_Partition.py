'''
Equal Subset Sum Partition

Given a set of positive numbers, find if we can partition it into two subsets such that
the sum of elements in both subsets is equal.
'''


def can_partition(nums):
    s = sum(nums)

    if s % 2 == 1:
        return False

    memo = {}
    return can_partition_recursive(nums, s // 2, 0, memo)


def can_partition_recursive(nums, target_sum, index, memo):
    if target_sum == 0:
        return True

    if len(nums) == 0 or index >= len(nums):
        return False


    if (target_sum, index) in memo:
        return memo[(target_sum, index)]

    can1, can2 = False, False
    if nums[index] <= target_sum:
        can1 = can_partition_recursive(nums, target_sum - nums[index], index + 1, memo)

    can2 = can_partition_recursive(nums, target_sum, index + 1, memo)
    memo[(target_sum, index)] = can1 or can2

    return memo[(target_sum, index)]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
