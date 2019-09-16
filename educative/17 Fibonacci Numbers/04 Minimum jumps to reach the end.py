'''
Minimum jumps to reach the end

Given an array of positive numbers, where each element represents the max number of jumps that can be made forward
from that element, write a program to find the minimum number of jumps needed to reach the end of the array (starting
from the first element). If an element is 0, then we cannot move through that element.
'''

import math


def minJumps(arr):
    memo = [-1 for _ in range(len(arr))]
    return helper(arr, 0, memo)


def helper(arr, index, memo):
    if index == len(arr) - 1:
        return 0

    if index >= len(arr) or arr[index] == 0:
        return math.inf

    if memo[index] == -1:
        maxJumps = arr[index]
        ans = math.inf

        for jump in range(1, maxJumps + 1):
            ans = min(ans, helper(arr, index + jump, memo))

        memo[index] = 1 + ans

    return memo[index]


print(minJumps([2, 1, 1, 1, 4]))
print(minJumps([1, 1, 3, 6, 9, 3, 0, 1, 3]))



