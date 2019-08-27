'''
K-Messed Array Sort
'''

from heapq import *


def sort_k_messed_array(arr, k):
    if len(arr) <= k:
        return arr

    result = []
    min_heap = []
    i = 0

    for _ in range(k + 1):
        heappush(min_heap, arr[i])
        i += 1

    result.append(heappop(min_heap))

    while i < len(arr):
        heappush(min_heap, arr[i])
        result.append(heappop(min_heap))
        i += 1

    while min_heap:
        result.append(heappop(min_heap))

    return result


arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k = 4
print(sort_k_messed_array(arr, k))


