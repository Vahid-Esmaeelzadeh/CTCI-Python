'''
Conversion : Write a function to determine the number of bits you would need to flip to convert
integer A to integer B.

EXAMPLE
Input: 29 (or: 11101), 15 (or: 01111)
Output: 2
'''


def conversionBitsCount(a: int, b: int):
    c = a ^ b
    count = 0
    while c != 0:
        c = c & (c-1)
        count += 1

    return count

a = 123
b = 654

print(bin(a), bin(b))
print(conversionBitsCount(a, b))