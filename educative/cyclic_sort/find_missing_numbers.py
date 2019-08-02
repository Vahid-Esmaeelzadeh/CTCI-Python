def find_missing_numbers(nums):
    i, n = 0, len(nums)
    result = []

    while i < n:
        val = nums[i] - 1
        if nums[val] != nums[i]:
            nums[val], nums[i] = nums[i], nums[val]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            result.append(i + 1)

    return result


a = [2, 3, 1, 8, 2, 3, 5, 1]
b = [2, 2, 2, 2]
print(find_missing_numbers(a))
print(a)
print(find_missing_numbers(b))
print(b)