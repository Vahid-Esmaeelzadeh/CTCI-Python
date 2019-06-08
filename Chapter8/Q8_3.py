# Question 8.3 (Magic Index)

# region Distinct values
def magicIndex(lst: list):
    return magicIndex_helper(lst, 0, len(lst) - 1)


def magicIndex_helper(lst: list, start, end):
    # at the end, both start and end will be equal, so,
    # for two cases: (mid = start = end)
    # magicIndex_helper(lst, mid+1, mid) => mid+1 > mid
    # magicIndex_helper(lst, mid, mid-1) => mid > mid-1
    if start > end:
        return -1

    mid = (start + end) // 2

    if lst[mid] == mid:
        return mid
    if lst[mid] < mid:
        return magicIndex_helper(lst, mid+1, end)
    else:
        return magicIndex_helper(lst, start, mid - 1)


lst = [0, 2, 4, 5, 7, 10, 20]
print(magicIndex(lst))
# endregion

# region Repetitive values
def magicIndex2(lst: list):
    return magicIndex_helper2(lst, 0, len(lst) - 1)

def magicIndex_helper2(lst: list, start, end):
    if start > end:
        return -1

    midIndex = (start + end) // 2
    midValue = lst[midIndex]

    if midIndex == midValue:
        return midIndex

    leftIndex = min(midIndex - 1, midValue)
    left = magicIndex_helper(lst, start, leftIndex)

    if left >= 0:
        return left

    rightIndex = max(midIndex + 1, midValue)
    right = magicIndex_helper(lst, rightIndex, end)

    return right

lst = [-10, 2, 3, 4, 5, 10, 12, 12, 12, 12]
print(magicIndex(lst))

# endregion