def subsets_with_duplicates(nums):
    subsets = [[]]

    for currentNumber in nums:
        n = len(subsets)
        for i in range(n):
            set = list(subsets[i])
            set.append(currentNumber)
            if set not in subsets:
                subsets.append(set)

    return subsets


print(subsets_with_duplicates([1, 5, 3, 3]))
