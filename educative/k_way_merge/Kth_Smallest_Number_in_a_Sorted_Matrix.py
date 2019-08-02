'''
Kth Smallest Number in a Sorted Matrix

Given an N∗N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.
'''

from heapq import *


def find_kth_smallest(matrix, k):
    min_heap = []

    for i in range(min(k, len(matrix))):
        heappush(min_heap, (matrix[i][0], 0, matrix[i]))

    num = 0
    while min_heap:
        num, i, row = heappop(min_heap)
        k -= 1
        if k == 0:
            return num

        if len(row) > i + 1:
            heappush(min_heap, (row[i + 1], i + 1, row))

    return num


def main():
    print("Kth smallest number is: " +
          str(find_kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()
