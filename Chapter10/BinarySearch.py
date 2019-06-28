def binary_search(lst, x):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if x == lst[mid]:
            return mid
        elif x > lst[mid]:
            left = mid + 1
        elif x < lst[mid]:
            right = mid - 1

    return -1


def binary_search1(lst, x):
    return binary_search_rcr(lst, x, 0, len(lst) - 1)


def binary_search_rcr(lst, x, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if lst[mid] == x:
        return mid
    elif lst[mid] < x:
        return binary_search_rcr(lst, x, mid + 1, right)
    elif lst[mid] > x:
        return binary_search_rcr(lst, x, left, mid - 1)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(a, 1))
print(binary_search1(a, 23))