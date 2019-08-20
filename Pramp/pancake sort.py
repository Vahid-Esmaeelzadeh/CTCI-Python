'''
Pancake Sort
Given an array of integers arr:

Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
Write a function pancakeSort(arr) that sorts and returns the input array.
You are allowed to use only the function flip you wrote in the first step in order to make changes in the array.
Example:

input:  arr = [1, 5, 4, 3, 2]

output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
'''


def pancake_sort(arr):
    for j in range(len(arr)):
        # max_index = 0
        # for i in range(len(arr) - j):
        #     if arr[i] >= arr[max_index]:
        #         max_index = i
        max_index = find_max_index_in_prefix(arr, len(arr) - j)
        flip(arr, max_index + 1)
        flip(arr, len(arr) - j)


def flip(arr, k):
    for i in range(k // 2):
        arr[i], arr[k - i - 1] = arr[k - i - 1], arr[i]


def find_max_index_in_prefix(arr, k):
    max_index = 0
    for i in range(k):
        if arr[i] >= arr[max_index]:
            max_index = i
    return max_index


a = [4, 5, 0, 10, 100, 23, 7, -30]
pancake_sort(a)
print(a)