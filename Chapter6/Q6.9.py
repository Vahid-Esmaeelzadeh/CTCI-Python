def openLockers(n):
    lockers = [False] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            lockers[j] = lockers[j] ^ True
    return lockers[1:]


print(openLockers(100).count(True))
