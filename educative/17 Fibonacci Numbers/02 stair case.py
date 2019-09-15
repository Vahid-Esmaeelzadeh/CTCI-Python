'''
Stair case
'''


def count_ways(n):
    if n == 0:
        return 1  # base case, we don't need to take any step, so there is only one way

    if n == 1:
        return 1  # we can take one step to reach the end, and that is the only way

    if n == 2:
        return 2  # we can take one step twice or jump two steps to reach at the top

    # if we take 1 step, we are left with 'n-1' steps;
    take1Step = count_ways(n - 1)
    # similarly, if we took 2 steps, we are left with 'n-2' steps;
    take2Step = count_ways(n - 2)
    # if we took 3 steps, we are left with 'n-3' steps;
    take3Step = count_ways(n - 3)

    return take1Step + take2Step + take3Step


def count_ways1(n):
    if n < 2:
        return 1
    if n == 2:
        return 2
    n1, n2, n3 = 1, 1, 2
    for i in range(3, n + 1):
        n1, n2, n3 = n2, n3, n1 + n2 + n3
    return n3


def main():
    print(count_ways(3))
    print(count_ways(4))
    print(count_ways(5))


main()
