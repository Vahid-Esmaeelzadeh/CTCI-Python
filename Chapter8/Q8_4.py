#region Question 8.4 (power set)
def getAllSubsets(lst):
    if not lst:
        return [[]]
    outlist = getAllSubsets(lst[1:])
    '''
    for rest in outlist
        withFirst += lst[0] + rest
    '''
    withFirst = [[lst[0]] + rest for rest in outlist]
    withoutFirst = outlist
    return withoutFirst + withFirst


def powerset(lst):
    n = 1 << len(lst)
    allsubsets = []

    for i in range(n):
        subset = int2set(lst, i)
        allsubsets += [subset]
        #allsubsets.append(subset)
    return allsubsets
def int2set(lst, i):
    subset = []
    k = i
    index = 0
    while k > 0:
        if (k & 1) == 1:
            subset += [lst[index]]
            #subset.append(lst[index])
        index += 1
        k >>= 1
    return subset


set_in = [1, 2, 3]
print(getAllSubsets(set_in))
print (powerset(set_in))
#endregion
