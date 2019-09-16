'''
Minimum jumps with fee

Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing the fee that you have to pay if you take
the step. Implement a method to calculate the minimum fee required to reach the top of the staircase. At every step,
you have an option to take either 1 step, 2 steps, or 3 steps. You should assume that you are standing at the first
step.
'''


def find_min_fee(fee):
    return find_min_fee_recursive(fee, 0)


def find_min_fee_recursive(fee, currentIndex):
    n = len(fee)
    if currentIndex > n - 1:
        return 0

    # if we take 1 step, we are left with 'n-1' steps;
    take1Step = find_min_fee_recursive(fee, currentIndex + 1)
    # similarly, if we took 2 steps, we are left with 'n-2' steps;
    take2Step = find_min_fee_recursive(fee, currentIndex + 2)
    # if we took 3 steps, we are left with 'n-3' steps;
    take3Step = find_min_fee_recursive(fee, currentIndex + 3)

    _min = min(min(take1Step, take2Step), take3Step)

    return _min + fee[currentIndex]


def main():
    print(find_min_fee([1, 2, 5, 2, 1, 2]))
    print(find_min_fee([2, 3, 4, 5]))


main()
