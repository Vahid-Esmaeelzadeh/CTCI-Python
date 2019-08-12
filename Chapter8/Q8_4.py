'''
Power Set: Write a method to return all subsets of a set.
'''

# recursive solution
def getAllSubsets(lst):
    if len(lst) == 0:
        return [[]]
    outlist = getAllSubsets(lst[1:])

    '''
    for rest in outlist
        withFirst += lst[0] + rest
    '''
    withFirst = [[lst[0]] + rest for rest in outlist]
    withoutFirst = outlist
    return withoutFirst + withFirst
# endregion


# iterative solution
def powerset(lst):
    n = 1 << len(lst)
    allsubsets = []

    for i in range(n):
        subset = int2set(lst, i)
        allsubsets.append(subset)
    return allsubsets


def int2set(lst, i):
    subset = []
    index = 0
    while i > 0:
        if (i & 1) == 1:
            #subset += [lst[index]]
            subset.append(lst[index])
        index += 1
        i >>= 1
    return subset
# endregion


set_in = [1, 2, 3]
print(getAllSubsets(set_in))
print(powerset(set_in))


a = [[1, 2, 3]]
a += [[4, 5, 6]]
a.append(20)
print(a)


