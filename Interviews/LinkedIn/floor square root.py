'''
floor sqrt
'''


def floorSqrt(x):
    ans = None
    # Base cases
    if x == 0 or x == 1:
        return x

        # Do Binary Search for floor(sqrt(x))
    start = 1
    end = x / 2
    while start <= end:
        mid = (start + end) // 2

        # If x is a perfect square
        if mid * mid == x:
            return mid

        if mid * mid < x:
            start = mid + 1
            ans = mid
        else:
            # If mid*mid is greater than x
            end = mid - 1

    return ans


# driver code
x = 11
print(floorSqrt(x))
