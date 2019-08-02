def find_duplicate_number(nums):
    i, n = 0, len(nums)

    while i < n:
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[j] != nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
            else:
                return nums[i]
        else:
            i += 1

    return -1


print(find_duplicate_number([1, 4, 4, 3, 2]))
print(find_duplicate_number([2, 1, 3, 3, 5, 4]))
print(find_duplicate_number([2, 5, 1, 3, 4]))
