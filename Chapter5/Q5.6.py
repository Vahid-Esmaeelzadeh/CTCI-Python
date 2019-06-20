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