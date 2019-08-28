'''
K closets numbers to X

Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array.
Return the numbers in the sorted order.

Example 1:
Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]

Example 2:
Input: [2, 4, 5, 6, 9], K = 3, X = 6
Output: [4, 5, 6]

Example 3:
Input: [2, 4, 5, 6, 9], K = 3, X = 10
Output: [5, 6, 9]
'''
from heapq import *
from collections import deque


def find_closest_elements(arr, K, X):
    index = binary_search(arr, X)
    low, high = index - K, index + K

    low = max(low, 0)  # 'low' should not be less than zero
    # 'high' should not be greater the size of the array
    high = min(high, len(arr) - 1)

    minHeap = []
    # add all candidate elements to the min heap, sorted by their absolute difference from 'X'
    for i in range(low, high + 1):
        heappush(minHeap, (abs(arr[i] - X), arr[i]))

    # we need the top 'K' elements having smallest difference from 'X'
    result = []
    for _ in range(K):
        result.append(heappop(minHeap)[1])

    result.sort()
    return result


def find_closest_elements2(arr, K, X):
    result = deque()
    index = binary_search(arr, X)
    leftPointer, rightPointer = index, index + 1
    n = len(arr)
    for i in range(K):
        if leftPointer >= 0 and rightPointer < n:
            diff1 = abs(X - arr[leftPointer])
            diff2 = abs(X - arr[rightPointer])
            if diff1 <= diff2:
                result.appendleft(arr[leftPointer])
                leftPointer -= 1
            else:
                result.append(arr[rightPointer])
                rightPointer += 1
        elif leftPointer >= 0:
            result.appendleft(arr[leftPointer])
            leftPointer -= 1
        elif rightPointer < n:
            result.append(arr[rightPointer])
            rightPointer += 1

    return result


def binary_search(arr, target):
    if target < arr[0]:
        return 0
    if target > arr[-1]:
        return len(arr) - 1

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = int(low + (high - low) / 2)
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if arr[low] - target < target - arr[high]:
        return low
    return high
    # if low > 0:
    #     return low - 1
    # return low


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 8, 9], 3, 15)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))

    print()

    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 8, 9], 3, 15)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))

    print(binary_search([1, 4, 7], 3))

main()
