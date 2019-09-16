'''
House thief

There are ‘n’ houses built in a line. A thief wants to steal maximum possible money from these houses.
The only restriction the thief has is that he can’t steal from two consecutive houses, as that would alert the
security system. How should the thief maximize his stealing?

Problem Statement
Given a number array representing the wealth of ‘n’ houses, determine the maximum amount of money the thief
can steal without alerting the security system.
'''


def find_max_steal(arr):
    return helper(arr, 0)


def helper(arr, index):
    if index >= len(arr):
        return 0

    stealCurrent = arr[index] + helper(arr, index + 2)
    skipCurrent = helper(arr, index + 1)

    return max(stealCurrent, skipCurrent)


print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
print(find_max_steal([2, 10, 14, 8, 1]))
