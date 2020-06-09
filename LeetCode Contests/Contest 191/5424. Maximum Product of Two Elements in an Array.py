# 5424. Maximum Product of Two Elements in an Array
from heapq import *

def maxProduct(nums):
    min_heap = []

    for i in range(len(nums)):
        heappush(min_heap, nums[i])

        if len(min_heap) > 2:
            heappop(min_heap)

    num1 = heappop(min_heap)
    num2 = heappop(min_heap)

    return (num1 - 1)*(num2 - 1)

print(maxProduct( [1,5,4,5]))
