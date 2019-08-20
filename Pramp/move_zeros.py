'''
Move Zeros To End
Given a static-sized array of integers arr, move all zeroes in the array to the end of the array.
You should preserve the relative order of items in the array.

We should implement a solution that is more efficient than a naive brute force.

Examples:

input:  arr = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
output: [1, 10, 2, 8, 3, 6, 4, 5, 7, 0, 0, 0, 0, 0]

'''


def move_zeros(arr):
    write_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[write_index], arr[i] = arr[i], arr[write_index]
            write_index += 1


a = [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]
move_zeros(a)
print(a)