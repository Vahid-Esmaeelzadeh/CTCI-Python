'''
Kth largest element in a stream of numbers

Design a class to efficiently find the Kth largest element in a stream of numbers.

The class should have the following two things:

The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
The class should expose a function add(int num) which will store the given number and return the Kth largest number.

Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 4
1. Calling add(6) should return '5'.
2. Calling add(13) should return '6'.
3. Calling add(4) should still return '6'.
'''

from heapq import *


class KthLargestNumberInStream2:
    minHeap = []

    def __init__(self, nums, k):
        self.k = k
        # add the numbers in the min heap
        for num in nums:
            self.add(num)

    def add(self, num):
        # add the new number in the min heap
        heappush(self.minHeap, num)

        # if heap has more than 'k' numbers, remove one number
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)

        # return the 'Kth largest number
        return self.minHeap[0]


class KthLargestNumberInStream:
    max_heap = []

    def __init__(self, nums, k):
        #self.nums = nums
        for x in nums:
            heappush(self.max_heap, -x)
        self.k = k

    def add(self, num):
        #self.nums.append(num)
        heappush(self.max_heap, -num)
        temp_items = []
        for _ in range(self.k):
            temp_items.append(heappop(self.max_heap))
        for x in temp_items:
            heappush(self.max_heap, x)

        return -temp_items[-1]



def main():
    kthLargestNumber = KthLargestNumberInStream2([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()
