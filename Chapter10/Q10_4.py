'''
Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size
method. It does, however, have an elementAt(i) method that returns the element at index i in
0(1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data
structure only supports positive integers.) Given a Listy which contains sorted, positive integers,
fnd the index at which an element x occurs. If x occurs multiple times, you may return any index.
'''


class Listy:
    def __init__(self, lst):
        self._list = lst

    def element_at(self, i):
        if 0 <= i < len(self._list):
            return self._list[i]
        else:
            return -1


def search(a: Listy, x):
    index = 1
    while a.element_at(index) != -1 and a.element_at(index) < x:
        index *= 2
    return bsearch(a, x, index // 2, index)


def bsearch(a, x, left, right):
    mid = -1

    while left <= right:
        mid = (left + right) // 2
        mid_val = a.element_at(mid)

        if mid_val == x:
            return mid
        elif x < mid_val or mid_val == -1:
            right = mid - 1
        elif x > mid_val:
            left = mid + 1

    return -1


lst = Listy([1, 4, 7, 9, 12, 14])
print(search(lst, 14))

print("\nbuilt-in search functions:\n")
s = [1, 3, 4, 5, 5, 5]

gen = (x for x in s if x < 4)
print(next(gen))
print(next(gen))

print([x for x in s if x > 4])
print([i for i, x in enumerate(s) if x == 5])

