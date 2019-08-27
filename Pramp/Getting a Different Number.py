'''
Getting a Different Number

Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest
nonnegative integer that is NOT in the array.
'''


def get_different_number(arr):
    n = len(arr)
    i = 0

    while i < n:
        val = arr[i]
        if val != i and val < n:
            arr[val], arr[i] = arr[i], arr[val]
        else:
            i += 1

    for i in range(n):
        if i != arr[i]:
            return i

    return n


arr = [0, 100, 2, 3]
print(get_different_number(arr))
