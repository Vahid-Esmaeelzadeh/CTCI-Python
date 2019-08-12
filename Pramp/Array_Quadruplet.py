'''
Array Quadruplet (Four-Sum)
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers
(quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order.
If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you
encounter (considering the results are sorted).
'''


def find_array_quadruplet(arr, s):
    n = len(arr)
    if n < 4:
        return []

    arr.sort()

    for i in range(0, n - 3):
        for j in range(i + 1, n - 2):
            p1 = j + 1
            p2 = n - 1

            while p1 < p2:
                if arr[i] + arr[j] + arr[p1] + arr[p2] == s:
                    return [arr[i], arr[j], arr[p1], arr[p2]]
                elif arr[i] + arr[j] + arr[p1] + arr[p2] < s:
                    p1 += 1
                else:
                    p2 -= 1

    return []


arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20

print(find_array_quadruplet(arr, s))