'''
Top k frequent numbers

Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.
'''

from heapq import *


def find_top_k_frequent_numbers(nums, k):
    num_freq_map = {}

    for num in nums:
        num_freq_map[num] = num_freq_map.get(num, 0) + 1

    min_heap = []

    for num, freq in num_freq_map.items():
        heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heappop(min_heap)

    result = []
    while min_heap:
        result.append(heappop(min_heap)[1])

    return result


print("Here are the K frequent numbers: " +
      str(find_top_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

print("Here are the K frequent numbers: " +
      str(find_top_k_frequent_numbers([5, 13, 13, 12, 12, 12, 11, 3, 11], 3)))
