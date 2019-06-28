import random


def quick_sort(arr):
    quick_sort_rcr(arr, 0, len(arr) - 1)


def quick_sort_rcr(arr, left, right):
    if left < right:
        p = partition(arr, left, right)
        quick_sort_rcr(arr, left, p - 1)
        quick_sort_rcr(arr, p, right)


def partition(arr, left, right):
    pivot_val = arr[(left + right) // 2]

    while left <= right:
        while arr[left] < pivot_val:
            left += 1

        while arr[right] > pivot_val:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left


lst = [random.randint(0, 100) for _ in range(20)]
print(lst)
quick_sort(lst)
print(lst)
