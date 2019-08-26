'''
radix sort
bucket sort
'''

import random
import copy


def radix_sort(lst):
    digit_num = len(str(max(lst)))
    for i in range(digit_num):
        sort_digit_based(lst, i)


def sort_digit_based(lst, i):
    count = [0 for _ in range(10)]
    result = [0 for _ in range(len(lst))]

    for x in lst:
        count[(x // (10 ** i)) % 10] += 1

    for k in range(1, 10):
        count[k] += count[k - 1]

    k = len(lst) - 1
    while k >= 0:
        c_index = (lst[k] // (10 ** i)) % 10
        result[count[c_index] - 1] = lst[k]
        count[c_index] -= 1
        k -= 1
    # we cannot write  lst = result
    for k in range(len(lst)):
        lst[k] = result[k]

    print(id(lst))


a = [random.randint(0, 1000) for _ in range(100)]
print(id(a))
print(a)
radix_sort(a)
print(a)


