'''
All Paths for a Sum

Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that
the sum of all the node values of each path equals ‘S’.
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_all_paths(root, s):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        if s == root.val:
            return 1
        return 0

    return count_all_paths(root.left, s - root.val) + count_all_paths(root.right, s - root.val)


def find_paths(root, sum):
    allPaths = []
    find_paths_recursive(root, sum, [], allPaths)
    return allPaths


def find_paths_recursive(currentNode, sum, currentPath, allPaths):
    if currentNode is None:
        return

    # add the current node to the path
    currentPath.append(currentNode.val)

    # if the current node is a leaf and its value is equal to sum, save the current path
    if currentNode.val == sum and currentNode.left is None and currentNode.right is None:
        allPaths.append(list(currentPath))
    else:
        # traverse the left sub-tree
        find_paths_recursive(currentNode.left, sum - currentNode.val, currentPath, allPaths)
        # traverse the right sub-tree
        find_paths_recursive(currentNode.right, sum - currentNode.val, currentPath, allPaths)

    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack.
    del currentPath[-1]  # we should not change the currentPath at each call


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))

    print(count_all_paths(root, sum))

main()
