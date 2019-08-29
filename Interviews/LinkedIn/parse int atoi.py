'''
parseInt
atoi
'''


def myAtoi(string):
    res = 0
    # initialize sign as positive
    sign = 1
    i = 0

    # skip all leading spaces
    while string[i] == " ":
        i += 1

    # if update the sign
    if string[i] == '-':
        sign = -1
        i += 1
    if string[i] == '+':
        sign = 1
        i += 1
    # Iterate through all characters of input string and update result
    for j in range(i, len(string)):
        # res = res * 10 + (ord(string[j]) - ord('0'))
        if not string[j].isdigit():
            return "ERROR"
        res = res * 10 + int(string[j])

    return sign * res


def atoi(str):
    if len(str) == 1:
        return int(str)

    return int(str[-1]) + 10 * atoi(str[0:len(str)-1])

print(myAtoi("   +1270"))

print(atoi("1270"))