# 1452. People Whose List of Favorite Companies Is Not a Subset of Another List


def peopleIndexes(favoriteCompanies):
    n = len(favoriteCompanies)
    result = []
    for i in range(n):
        count = 0
        for j in range(n):
            if i != j and isSubset(set(favoriteCompanies[i]), set(favoriteCompanies[j])):
                count += 1
                break
        if count == 0:
            result.append(i)

    return result


def isSubset(set1, set2):
    if len(set1) >= len(set2):
        return False

    for item in set1:
        if item not in set2:
            return False

    return True


favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
favoriteCompanies1 = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
favoriteCompanies2 = [["leetcode"],["google"],["facebook"],["amazon"]]
print(peopleIndexes(favoriteCompanies))
print(peopleIndexes(favoriteCompanies1))
print(peopleIndexes(favoriteCompanies2))
