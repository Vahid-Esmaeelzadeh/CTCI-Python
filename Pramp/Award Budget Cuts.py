'''
Award Budget Cuts

'''


def find_grants_cap(grantsArray, newBudget):
    n = len(grantsArray)

    # grants = [0 for i in range(n)]
    grantsArray.sort()

    i = 0

    while i < n:
        if grantsArray[i] <= (newBudget + 0.0) / (n - i):
            # grants[i] = grantsArray[i]
            newBudget -= grantsArray[i]
            i += 1
        else:
            newBudget = (newBudget + 0.0) / (n - i)
            # for j in range(i, n):
            # grants[j] = newBudget
            break

    return newBudget


grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190
print(find_grants_cap(grantsArray, newBudget))
