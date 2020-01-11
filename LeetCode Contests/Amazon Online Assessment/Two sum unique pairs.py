'''
Two sum - count of unique pairs
'''


def pair_with_target_sum2(arr, target_sum):
    num_set = set()
    pairs_set = set()

    for num in arr:
        if target_sum - num in num_set:
            pairs_set.add((max(num, target_sum - num), min(num, target_sum - num)))
        else:
            num_set.add(num)

    return len(pairs_set)


nums = [1, 1, 3, 44, 2, 45, 46, 46]
target = 47

nums1 = [1, 5, 1, 5]
target1 = 6

print(pair_with_target_sum2(nums, target))
