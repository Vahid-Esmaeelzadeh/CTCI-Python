def find_duplicate_numbers(nums):
    i, n = 0, len(nums)

    duplicate_nums = []

    while i < n:
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[j] != nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
            else:
                duplicate_nums.append(nums[i])
                i += 1
        else:
            i += 1

    return duplicate_nums


print(find_duplicate_numbers([3, 4, 4, 5, 5]))
print(find_duplicate_numbers([5, 4, 7, 2, 3, 5, 3]))