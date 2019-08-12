'''
Binary to String: Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
print the binary representation. If the number cannot be represented accurately in binary with at
most 32 characters, print "ERROR"
'''


def doubleTobin(f: float) -> str:
    count = 0
    binStr = str(bin(int(f))) + "."

    f = f - int(f)

    while count < 32:
        f = f * 2
        binStr += str(int(f))
        f = f - int(f)

        if f == 0:
            return binStr

        count += 1

    return "ERROR"



a = 123 + 1/8 + 1/32 + 1/64 + 1/128
print(doubleTobin(a))


