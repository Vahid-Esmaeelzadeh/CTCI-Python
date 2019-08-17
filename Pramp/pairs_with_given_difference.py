'''
Pairs with specific difference
'''


def find_pairs_with_given_difference(arr, k):
    result = []
    hash_map = {}

    for x in arr:
        hash_map[x - k] = x

    for y in arr:
        if y in hash_map:
            result.append([hash_map[y], y])

    return result




a = [0, -1, -2, 2, 1]
k = 1

print(find_pairs_with_given_difference(a, k))






