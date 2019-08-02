from heapq import *


class MedianOfStream:
    max_heap = []  # to store the first half of numbers
    min_heap = []  # to store the second half of numbers

    def insert_num(self, num):
        if not self.max_heap or num < -self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # balance two heaps
        if len(self.max_heap) - len(self.min_heap) > 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]


medianOfAStream = MedianOfStream()
medianOfAStream.insert_num(3)
medianOfAStream.insert_num(1)
print("The median is: " + str(medianOfAStream.find_median()))
medianOfAStream.insert_num(5)
print("The median is: " + str(medianOfAStream.find_median()))
medianOfAStream.insert_num(4)
print("The median is: " + str(medianOfAStream.find_median()))
