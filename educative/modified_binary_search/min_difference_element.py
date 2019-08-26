'''

Minimum Difference Element

Given an array of numbers sorted in ascending order, find the element in the array
that has the minimum difference with the given ‘key’.

Example 1:
Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array

Example 2:
Input: [4, 6, 10], key = 4
Output: 4
'''

import math


def search_min_diff_element2(arr, key):
    if key < arr[0]:
        return arr[0]
    if key > arr[-1]:
        return arr[-1]

    start, end = 0, len(arr) - 1

    while start <= end:

        mid = start + (end - start) // 2

        if key == arr[mid]:
            return arr[mid]
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    # if we are here, it means we did not find the key, and end < start and key is in between
    # arr[end] < key < arr[start]

    if (arr[start] - key) < (key - arr[end]):
        return arr[start]
    return arr[end]


def search_min_diff_element(arr, key):
    start, end = 0, len(arr) - 1
    diff = math.inf
    diff_index = -1

    while start <= end:

        mid = start + (end - start) // 2
        new_diff = abs(key - arr[mid])
        if new_diff < diff:
            diff = new_diff
            diff_index = mid

        if key == arr[mid]:
            return arr[mid]
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return arr[diff_index] if diff != math.inf else -1


def main():
    print(search_min_diff_element2([4, 6, 10], 7))
    print(search_min_diff_element2([4, 6, 10], 4))
    print(search_min_diff_element2([1, 3, 8, 10, 15], 14))
    print(search_min_diff_element2([4, 6, 10], 17))


main()
