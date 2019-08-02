'''
Remove Duplicates

Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space;
after removing the duplicates in-place return the new length of the array.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

'''


def remove_duplicates(arr):
    current = 0
    runner = 1

    while runner < len(arr):
        if arr[runner] != arr[current]:
            current += 1
            arr[current] = arr[runner]
        runner += 1

    return current + 1


a = [2, 3, 3, 3, 6, 9, 9, 9, 9, 10, 10, 11, 11, 12]
b = [1, 2, 3, 4, 5]
print(remove_duplicates(a))
print(a)

print(remove_duplicates([]))
print(b)


'''
remove all instances of ‘key’ in-place 
'''


def remove_element(arr, key):
    nextElement = 0  # index of the next element which is not 'key'
    for i in range(len(arr)):
        if arr[i] != key:
            arr[nextElement] = arr[i]
            nextElement += 1

    return nextElement


a = [2, 3, 3, 3, 6, 9, 9, 9, 9, 10, 10, 11, 11, 12]
b = [1, 2, 3, 4, 5]
print(remove_element(a, 3))
print(a)

print(remove_element(b, 4))
print(b)
