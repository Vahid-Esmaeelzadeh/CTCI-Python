'''
Pair with Target Sum
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
'''


# Using two pointers
def pair_with_target_sum(arr, target_sum):
    p1 = 0
    p2 = len(arr) - 1

    while p1 < p2:
        if arr[p1] + arr[p2] == target_sum:
            return [p1, p2]
        elif arr[p1] + arr[p2] < target_sum:
            p1 += 1
        else:
            p2 -= 1

    return [-1, -1]


# Using Hash Table
def pair_with_target_sum2(arr, target_sum):
    hash_table = {}  # to store {number, index}

    for i, num in enumerate(arr):
        if target_sum - num in hash_table:
            return [hash_table[target_sum - num], i]
        else:
            hash_table[num] = i

    return [-1, -1]


print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
print(pair_with_target_sum([2, 5, 9, 11], 11))
print(pair_with_target_sum2([1, 2, 3, 4, 6], 6))
print(pair_with_target_sum2([2, 5, 9, 11], 11))

