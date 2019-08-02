# using Hash set
def is_happy_number(num):
    num_set = set()
    while True:
        num = sum_of_squares_of_digits(num)
        if num == 1:
            return True
        if num in num_set:
            return False
        num_set.add(num)


# using slow and fast pointers
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


print(is_happy_number(23))
print(find_happy_number(23))