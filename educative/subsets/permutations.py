from collections import deque


def permutations(nums):
    if not nums:
        return None

    result = deque()
    result.append([nums[0]])

    for n in range(1, len(nums)):
        temp_len = len(result)
        for _ in range(temp_len):
            item = result.popleft()
            for i in range(len(item) + 1):
                result.append(item[:i] + [nums[n]] + item[i:])

    return list(result)


print(permutations([1, 2, 3]))
