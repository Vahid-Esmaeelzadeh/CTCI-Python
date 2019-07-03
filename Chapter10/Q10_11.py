import random
import sys


def sort_valley_peak(arr: list):
    arr.sort()
    for i in range(1, len(arr), 2):
        arr[i-1], arr[i] = arr[i], arr[i-1]


def sort_valley_peak2(arr: list):
    for i in range(1, len(arr), 2):
        biggest_index = max_index(arr, i-1, i, i+1)
        if i != biggest_index:
            arr[i], arr[biggest_index] = arr[biggest_index], arr[i]


def max_index(arr, i, j, k):
    length = len(arr)
    arr_i = arr[i] if 0 <= i < length else -sys.maxsize
    arr_j = arr[j] if 0 <= j < length else -sys.maxsize
    arr_k = arr[k] if 0 <= k < length else -sys.maxsize

    max_val = max(arr_i, arr_j, arr_k)

    if max_val == arr_i:
        return i
    elif max_val == arr_j:
        return j
    else:
        return k

a = [random.randint(0, 100) for _ in range(20)]
b = [random.randint(0, 100) for _ in range(20)]
print(a)
sort_valley_peak(a)
print(a)
print("--------------")
print(b)
sort_valley_peak2(b)
print(b)


