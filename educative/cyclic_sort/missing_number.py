def find_missing_number(nums):
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] < n and nums[i] != nums[nums[i]]:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        else:
            i += 1

    for k in range(n):
        if nums[k] != k:
            return k

    return n

def main():
    print(find_missing_number([2, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()
