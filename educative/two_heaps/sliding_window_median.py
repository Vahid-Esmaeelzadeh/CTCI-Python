from heapq import *
import heapq

def remove(heap, element):
    ind = heap.index(element)  # find the element
    # move the element to the end and delete it
    heap[ind] = heap[-1]
    del heap[-1]
    # we can use heapify to readjust the elements but that would be O(N),
    # instead, we will adjust only one element which will O(logN)
    if ind < len(heap):
        heapq._siftup(heap, ind)
        heapq._siftdown(heap, 0, ind)

q = [1, 2, 3, 4, 5]
remove(q, 3)
