'''
Subsets
Given a set with distinct elements, find all of its distinct subsets.
'''


def subsets(elements):
    result = [[]]

    for element in elements:
        result = result + [i + [element] for i in result]

    return result


def find_subsets(nums):
    subsets = []
    # start by adding the empty subset
    subsets.append([])
    for currentNumber in nums:
        # we will take all existing subsets and insert the current number in them to create new subsets
        n = len(subsets)
        for i in range(n):
            # create a new subset from the existing subset and insert the current element to it
            set = list(subsets[i])
            set.append(currentNumber)
            subsets.append(set)

    return subsets


print(subsets([1, 5, 3]))
print(find_subsets([1, 5, 3]))

print([3] + [5])