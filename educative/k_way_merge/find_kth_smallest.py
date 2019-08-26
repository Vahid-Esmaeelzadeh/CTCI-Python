'''
Kth Smallest Number in M Sorted Lists
Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.
'''

from heapq import *


def find_kth_smallest(lists, k):
    minHeap = []

    # put the 1st element of each list in the min heap
    for i in range(len(lists)):
        if len(lists[i]) > 0:
            heappush(minHeap, (lists[i][0], 0, lists[i]))

    # take the smallest(top) element form the min heap, if k == 0 return the number
    number = 0
    while minHeap:
        number, i, lst = heappop(minHeap)
        k -= 1
        if k == 0:
            break
        # if the array of the top element has more elements, add the next element to the heap
        if len(lst) > i + 1:
            heappush(minHeap, (lst[i + 1], i + 1, lst))

    return number


def main():
    print("Kth smallest number is: " +
          str(find_kth_smallest([[2, 6, 8], [3, 6, 7], []], 2)))


main()
