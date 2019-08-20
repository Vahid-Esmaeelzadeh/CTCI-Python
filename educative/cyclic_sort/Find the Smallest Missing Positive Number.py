'''
Find the Smallest Missing Positive Number

Given an unsorted array containing numbers, find the smallest missing positive number in it.

Example 1:

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'
'''


def find_first_missing_positive(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if 1 <= nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return nums.length + 1


def main():
    print(find_first_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_missing_positive([3, 2, 5, 1]))


main()
