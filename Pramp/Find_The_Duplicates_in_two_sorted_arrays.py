'''
Find duplicates

Find The Duplicates in two sorted arrays arr1 and arr2

Let N and M be the lengths of arr1 and arr2, respectively.
Solve for two cases and analyze the time & space complexities of your solutions:
I)  M ≈ N - the array lengths are approximately the same
II) M ≫ N - arr2 is much bigger than arr1.
'''

# region case (II) - O(NlogM)
def find_duplicates2(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    res = []

    shorter = []
    longer = []

    if n1 < n2:
        shorter = arr1
        longer = arr2
    else:
        shorter = arr2
        longer = arr1

    start = 0

    for x in shorter:
        ind = bsearch(longer, x, start)
        if ind != -1:
            res.append(x)
            start = ind

    return res


def bsearch(arr, x, start):
    low = start
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1
# endregion


# region case(I) - O(N + M)
def find_duplicates1(arr1, arr2):
    i, j = 0, 0
    res = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            res.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return res

# endregion


arr1 = [1, 2, 3, 5, 6, 7]
arr2 = [3, 6, 7, 8, 20]
print(find_duplicates1(arr1, arr2))
print(find_duplicates2(arr1, arr2))
