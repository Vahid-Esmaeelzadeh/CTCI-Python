'''
Happy Number
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square
 of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’.
 Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

Example 1:

Input: 23
Output: true (23 is a happy number)
Explanations: Here are the steps to find out that 23 is a happy number:
23 -> 13 -> 10 -> 1

Example 2:
Input: 12
Output: false (12 is not a happy number)
Explanations: Here are the steps to find out that 12 is not a happy number:
12 -> 5 -> 25 -> 29 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89  (cycle at 89)
'''


def sum_of_squares_of_digits(num):
    s = 0
    while num > 0:
        s += (num % 10) ** 2
        num = num // 10
    return s


def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = sum_of_squares_of_digits(slow)  # move one step
        fast = sum_of_squares_of_digits(sum_of_squares_of_digits(fast))  # move two steps

        if slow == fast:  # found the cycle
            break
    return slow == 1  # see if the cycle is stuck on the number '1'


print(find_happy_number(12))
