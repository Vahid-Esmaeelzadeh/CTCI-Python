'''
Subsets with duplicates
Given a set of numbers that might contain duplicates, find all of its distinct subsets.
'''


def subsets_with_dups(elements):
    result = [[]]

    for element in elements:
        new_subsets = [i + [element] for i in result]
        for j in new_subsets:
            if j not in result:
                #result = result + [j]
                result.append(j)

    return result


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
print(subsets_with_dups([1, 5, 3, 3]))

