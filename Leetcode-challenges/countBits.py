# count bits


def countBits(num):
    result = [0]
    for i in range(1, num + 1):
        n = i
        count = 1
        while n & (n-1) != 0:
            n = n & (n - 1)
            count += 1

        result.append(count)

    return result

print(countBits(2))