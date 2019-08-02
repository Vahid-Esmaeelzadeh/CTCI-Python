'''
Sum of elements

Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

Example 1:
Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
Output: 23

Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
between 5 and 15 is 23 (11+12).

Example 2:
Input: [3, 5, 8, 7], and K1=1, K2=4
Output: 12

Explanation: The sum of the numbers between the 1st smallest number (3) and the 4th smallest
number (8) is 12 (5+7).

'''

from heapq import *

# using  min-Heap
def find_sum_of_elements(nums, k1, k2):
    result = 0
    min_heap = []

    for num in nums:
        heappush(min_heap, num)

    i = 0
    while min_heap and i < k2:
        temp = heappop(min_heap)
        i += 1

        if k1 < i < k2:
            result += temp

    return result


# using max-heap
def find_sum_of_elements2(nums, k1, k2):
    maxHeap = []
    # keep smallest k2 numbers in the max heap
    for i in range(len(nums)):
        if i < k2 - 1:
            heappush(maxHeap, -nums[i])
        elif nums[i] < -maxHeap[0]:
            heappop(maxHeap)  # as we are interested only in the smallest k2 numbers
            heappush(maxHeap, -nums[i])

    # get the sum of numbers between k1 and k2 indices
    # these numbers will be at the top of the max heap
    elementSum = 0
    for _ in range(k2 - k1 - 1):
        elementSum += -heappop(maxHeap)

    return elementSum


def main():
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))

    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements2([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements2([3, 5, 8, 7], 1, 4)))


main()
