'''
Permutations - iterative (07 Tree BFS approach)
Given a set of distinct numbers, find all of its permutations.
'''

from collections import deque


def permutations(nums):
    if not nums:
        return None

    result = deque()
    result.append([nums[0]])

    for new_num in range(1, len(nums)):
        temp_len = len(result)
        for _ in range(temp_len):
            item = result.popleft()
            for i in range(len(item) + 1):
                result.append(item[:i] + [nums[new_num]] + item[i:])

    return list(result)


def permutations_recr(nums):
    if len(nums) == 0:
        return [[]]

    subPerm = permutations_recr(nums[1:])
    res = []

    for x in subPerm:
        for i in range(len(nums)):
            res.append(x[:i] + [nums[0]] + x[i:])

    return res


print(permutations([1, 2, 3]))
print(permutations_recr([1, 2, 3]))
