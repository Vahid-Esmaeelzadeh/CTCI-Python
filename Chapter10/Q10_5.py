'''
Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a
method to find the location of a given string.

EXAMPLE
Input: ball, {"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}
Output: 4
'''


def sparse_search(a, s):
    return sparse_search_rcr(a, s, 0, len(a) - 1)


def sparse_search_rcr(a, s, left, right):
    if left > right:
        return -1

    mid = calc_mid(a, left, right)

    if mid == -1:
        return mid
    if a[mid] == s:
        return mid
    if s < a[mid]:
        return sparse_search_rcr(a, s, left, mid - 1)
    if s > a[mid]:
        return sparse_search_rcr(a, s, mid + 1, right)


def calc_mid(a, left, right):
    mid = (left + right) // 2

    if a[mid] != "":
        return mid

    i = 1
    while True:
        if mid - i < left and mid + i > right:
            return -1
        if mid - i >= left and a[mid - i] != "":
            return mid - i
        if mid + i <= right and a[mid + i] != "":
            return mid + i
        i += 1


arr = ["aaa", "", "", "", "", "", "bbb", "", "", "ccc", "", "ddd", "", "", "", "", "", "eee", "", ""]
print(sparse_search(arr, "eee"))
