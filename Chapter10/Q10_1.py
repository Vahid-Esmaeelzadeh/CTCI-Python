'''
Merge two sorted arrays
Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.
'''


def merge_b2a(arr_a, arr_b, last_a):
    ia = last_a - 1
    ib = len(arr_b) - 1
    im = last_a + len(arr_b) - 1

    # increase the size of array A if it does not have enough space
    while last_a + len(arr_b) > len(arr_a):
        arr_a.append(None)

    while ib >= 0:
        if ia >= 0 and arr_b[ib] < arr_a[ia]:
            arr_a[im] = arr_a[ia]
            ia -= 1
        else:
            arr_a[im] = arr_b[ib]
            ib -= 1
        im -= 1


lst1 = [1, 20, 30, 60]
lst2 = [-1, 10, 15, 56, 78, 80, 100, 400]

merge_b2a(lst1, lst2, 4)
print(lst1)