'''
Find Duplicates in Large array: You have an array with all the numbers from 1 to N, where N is at most 32,000. The
array may have duplicate entries and you do not know what N is. With only 4 kilobytes of memory
available, how would you print all duplicate elements in the array?
'''
import random


def find_duplicates(arr: list):
    num_freq = [0] * 1000  # each element has 32-bit length
    for num in arr:
        if num_freq[num >> 5] & 1 << (num & 0x1F) != 0:
            print(num, end=" ")
        else:
            num_freq[num >> 5] |= 1 << (num & 0x1F)


lst = [random.randint(0, 20) for _ in range(30)]
print(lst)
find_duplicates(lst)
print()


