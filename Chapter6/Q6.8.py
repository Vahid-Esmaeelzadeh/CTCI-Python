import sys
# Function to get minimum number of trials
# needed in worst case with n eggs and k floors  
def eggDrop(n, k):
    # If there are no floors, then no trials
    # needed. OR if there is one floor, one 
    # trial needed. 
    if k == 1 or k == 0:
        return k

    # We need k trials for one egg
    # and k floors 
    if n == 1:
        return k

    minVal = sys.maxsize

    # Consider all droppings from 1st  
    # floor to kth floor and return  
    # the minimum of these values plus 1. 
    for x in range(1, k + 1):

        res = max(eggDrop(n - 1, x - 1), eggDrop(n, k - x))
        if (res < minVal):
            minVal = res

    return minVal + 1

def eggDrop_DP(n, k):
    memo = dict()
    return eggDrop_rcr(n, k, memo)

def eggDrop_rcr(n, k, memo):
    # If there are no floors, then no trials
    # needed. OR if there is one floor, one
    # trial needed.
    if k == 1 or k == 0:
        return k

        # We need k trials for one egg
    # and k floors
    if n == 1:
        return k

    minVal = sys.maxsize

    # Consider all droppings from 1st
    # floor to kth floor and return
    # the minimum of these values plus 1.
    for x in range(1, k + 1):
        res1 = 0
        res2 = 0

        if (n - 1, x - 1) not in memo:
            res1 = eggDrop_rcr(n - 1, x - 1, memo)
            memo[(n - 1, x - 1)] = res1
        else:
            res1 = memo[(n - 1, x - 1)]

        if (n, k - x) not in memo:
            res2 = eggDrop_rcr(n, k - x, memo)
            memo[(n, k - x)] = res2
        else:
            res2 = memo[(n, k - x)]

        res = max(res1, res2)

        if res < minVal:
            minVal = res

    return minVal + 1

print(eggDrop_DP(2, 36))
