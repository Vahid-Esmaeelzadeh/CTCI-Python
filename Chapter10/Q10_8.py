from numpy import uint32
from numpy import uint16
from numpy import uint8
from sys import getsizeof
import random

def find_duplicates(arr: list):
    num_freq = [0] * 1000  # each element has 32-bit length
    for i in range(len(arr)):
        if num_freq[arr[i] >> 5] & 1 << (arr[i] & 0x1F) != 0:
            print(arr[i], end=" ")
        else:
            num_freq[arr[i] >> 5] |= 1 << (arr[i] & 0x1F)


lst = [random.randint(0, 20) for _ in range(30)]
print(lst)
find_duplicates(lst)
print()


