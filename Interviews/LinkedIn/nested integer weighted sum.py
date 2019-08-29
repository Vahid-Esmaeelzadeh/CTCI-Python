'''
Nested integer weighted sum
'''


def weighted_sum(lst):
    if lst is None or len(lst) == 0:
        return 0

    return helper(lst, 1)


def helper(lst, level):
    result = 0
    for x in lst:
        if not isinstance(x, list):
            result += x * level
        else:
            result += helper(x, level + 1)

    return result


lst = [1,[4,[6]]]
print(weighted_sum(lst))
