'''
Next Number: Given a positive integer, print the next smallest and the next largest number that
have the same number of 1 bits in their binary representation.
'''


def nextNumber(n: int):
    if n == 0:
        print("All zero input!")
        return
    if ~n == 0:
        print("All one input!")
        return

    i = 0
    smallPrinted = 0
    bigPrinted = 0
    a = n

    while a != 0:
        index1 = 1 << i
        index2 = 1 << (i + 1)

        if smallPrinted == 0 and (n & index1) == 0 and (n & index2) != 0:  # 10
            m = n | index1
            m = m & ~index2
            print("Next smaller number with same number of 1s: ", bin(m), m)
            smallPrinted = 1

        elif bigPrinted == 0 and (n & index2) == 0 and (n & index1) != 0:  # 01
            m = n | index2
            m = m & ~index1
            print("Next bigger number with same number of 1s: ", bin(m), m)
            bigPrinted = 1

        i += 1
        a = a >> 1

        if smallPrinted == 1 and bigPrinted == 1:
            return


num = 812736
print(bin(num), num)
nextNumber(num)

