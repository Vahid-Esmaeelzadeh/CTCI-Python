'''
Edit Distance
'''


# my solution
def find_edit_distance(s1, s2):
    n = find_LCS_length(s1, s2)
    return max(len(s1) - n, len(s2) - n)


def find_min_operations(s1, s2):
    return find_min_operations_recursive(s1, s2, 0, 0)


def find_min_operations_recursive(s1, s2, i1, i2):
    n1, n2 = len(s1), len(s2)
    # if we have reached the end of s1, then we have to insert all the remaining characters of s2
    if i1 == n1:
        return n2 - i2

    # if we have reached the end of s2, then we have to delete all the remaining characters of s1
    if i2 == n2:
        return n1 - i1

    # If the strings have a matching character, we can recursively match for the remaining lengths
    if s1[i1] == s2[i2]:
        return find_min_operations_recursive(s1, s2, i1 + 1, i2 + 1)

    # perform deletion
    c1 = 1 + find_min_operations_recursive(s1, s2, i1 + 1, i2)
    # perform insertion
    c2 = 1 + find_min_operations_recursive(s1, s2, i1, i2 + 1)
    # perform replacement
    c3 = 1 + find_min_operations_recursive(s1, s2, i1 + 1, i2 + 1)

    return min(c1, min(c2, c3))


def find_LCS_length(s1, s2):
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    return find_LCS_length_recursive(dp, s1, s2, 0, 0)


def find_LCS_length_recursive(dp, s1, s2, i1, i2):
    if i1 == len(s1) or i2 == len(s2):
        return 0

    if dp[i1][i2] == -1:
        if s1[i1] == s2[i2]:
            dp[i1][i2] = 1 + find_LCS_length_recursive(dp, s1, s2, i1 + 1, i2 + 1)
        else:
            c1 = find_LCS_length_recursive(dp, s1, s2, i1, i2 + 1)
            c2 = find_LCS_length_recursive(dp, s1, s2, i1 + 1, i2)
            dp[i1][i2] = max(c1, c2)

    return dp[i1][i2]


def main():
    print(find_min_operations("bat", "but"))
    print(find_min_operations("abdca", "cbda"))
    print(find_min_operations("passpot", "ppsspqrt"))
    print(find_min_operations("qqqbvaadskfj", "nvmfkl"))

    print()

    print(find_edit_distance("bat", "but"))
    print(find_edit_distance("abdca", "cbda"))
    print(find_edit_distance("passpot", "ppsspqrt"))
    print(find_edit_distance("qqqbvaadskfj", "nvmfkl"))

main()
