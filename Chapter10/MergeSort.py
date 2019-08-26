'''
Merge sort
'''

import random


def merge_sort(arr: list):
    if not arr:
        return None

    length = len(arr)

    if length == 0:
        return []
    if length == 1:
        return arr

    a = merge_sort(arr[:length // 2])
    b = merge_sort(arr[length // 2:])

    return merge(a, b)


def merge(a, b):
    result = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    if i < len(a):
        result += a[i:]

    if j < len(b):
        result += b[j:]

    return result


lst = merge_sort([random.randint(0, 100) for _ in range(20)])
print(lst)
