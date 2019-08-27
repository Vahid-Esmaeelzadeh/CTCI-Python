'''
Magic Index: A magic index in an array A [0..n -1] is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

FOLLOW UP
What if the values are not distinct?
'''

import math

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


# def minimum_magicIndex(lst: list):
#     return minimum_magicIndex_helper(lst, 0, len(lst) - 1)
#
#
# def minimum_magicIndex_helper(lst: list, start, end):
#     # at the end, both start and end will be equal, so,
#     # for two cases: (mid = start = end)
#     # magicIndex_helper(lst, mid+1, mid) => mid+1 > mid
#     # magicIndex_helper(lst, mid, mid-1) => mid > mid-1
#     if start > end:
#         return -1
#
#     mid = (start + end) // 2
#
#     if lst[mid] == mid:
#         if mid - 1 >= 0 and lst[mid - 1] < mid - 1:
#             return mid
#         return minimum_magicIndex_helper(lst, start, mid - 1)
#     if lst[mid] < mid:
#         return minimum_magicIndex_helper(lst, mid+1, end)
#     else:
#         return minimum_magicIndex_helper(lst, start, mid - 1)


lst = [0, 1, 3, 5, 7, 10, 20]
print(magicIndex(lst))
# print(minimum_magicIndex(lst))
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

    left = magicIndex_helper2(lst, start, min(midIndex - 1, midValue))

    if left >= 0:
        return left

    right = magicIndex_helper2(lst, max(midIndex + 1, midValue), end)

    return right

lst = [-10, 2, 3, 4, 5, 6, 7, 9, 9, 9]
print(magicIndex(lst))

