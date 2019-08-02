'''
Kth Smallest Number in M Sorted Lists
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.
'''

from heapq import *


def find_kth_smallest2(lists, k):
    minHeap = []

    # put the 1st element of each list in the min heap
    for i in range(len(lists)):
        if len(lists[i]) > 0:
            heappush(minHeap, (lists[i][0], 0, lists[i]))

    # take the smallest(top) element form the min heap, if k == 0 return the number
    number = 0
    while minHeap:
        number, i, list = heappop(minHeap)
        k -= 1
        if k == 0:
            break
        # if the array of the top element has more elements, add the next element to the heap
        if len(list) > i + 1:
            heappush(minHeap, (list[i + 1], i + 1, list))

    return number


def find_kth_smallest(lists, k):
    min_heap = []
    current_indices = [0] * len(lists)

    for i in range(len(lists)):
        if len(lists[i]) > current_indices[i]:
            heappush(min_heap, (lists[i][current_indices[i]], i))
            current_indices[i] += 1

    num = None
    while min_heap:
        num, i = heappop(min_heap)

        k -= 1
        if k == 0:
            break

        if len(lists[i]) > current_indices[i]:
            heappush(min_heap, (lists[i][current_indices[i]], i))
            current_indices[i] += 1


    return num

def main():
    print("Kth smallest number is: " +
          str(find_kth_smallest2([[2, 6, 8], [3, 6, 7], []], 2)))


main()
