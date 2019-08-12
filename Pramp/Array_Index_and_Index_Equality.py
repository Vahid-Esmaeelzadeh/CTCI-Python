'''
Array Index & Element Equality
Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i
 for which arr[i] == i. Return -1 if there is no such index.
'''

import sys


def index_equals_value_search(arr):

    min_val = sys.maxsize
    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == mid:
            min_val = min(min_val, mid)
            end = mid - 1
            if mid - 1 >= 0 and arr[mid - 1] < mid - 1:
                return min_val

        elif arr[mid] > mid:
            end = mid - 1

        else:
            start = mid + 1

    if min_val != sys.maxsize:
        return min_val

    return -1
