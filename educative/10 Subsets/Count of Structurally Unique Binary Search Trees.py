'''
Count of Structurally Unique Binary Search Trees

Given a number ‘n’, write a function to return the count of structurally unique Binary Search Trees (BST) that can
store values 1 to ‘n’.
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_trees(n):
    return count_trees_memo(n, {})


def count_trees_memo(n, memo):
    if n <= 1:
        return 1

    if n in memo:
        return memo[n]

    count = 0
    for i in range(1, n + 1):
        # making 'i' root of the tree
        countOfLeftSubtrees = count_trees(i - 1)
        countOfRightSubtrees = count_trees(n - i)
        # Ex. n = 5, i = 2,  [1 2 {3 4 5}]
        # it doesn't matter we count the number of right subtrees based on {3,4,5} or {1, 2, 3}.
        # That's why we can call the function with (n-i)

        count += (countOfLeftSubtrees * countOfRightSubtrees)

    memo[n] = count
    return count


def main():
    print("Total trees: " + str(count_trees(2)))
    print("Total trees: " + str(count_trees(3)))


main()
