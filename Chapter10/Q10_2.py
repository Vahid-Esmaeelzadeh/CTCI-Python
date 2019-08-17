'''
Group Anagrams: Write a method to sort an array ot strings so that all tne anagrams are next to
each other.
'''


def group_anagrams(lst):
    hash_map = dict()
    for x in lst:
        x_sorted = str(sorted(x))
        if x_sorted in hash_map:
            hash_map[x_sorted].append(x)
        else:
            hash_map[x_sorted] = [x]

    i = 0
    for x in hash_map:
        for s in hash_map[x]:
            lst[i] = s
            i += 1

a = ["Vahid", "HAPPY", "laheE", "dihaV", "Elahe"]
group_anagrams(a)
print(a)

a = [1, 2, 3, 4, 5, 6]
print(''.join(str(x) for x in a))
