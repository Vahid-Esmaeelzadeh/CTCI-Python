'''
The root-to-leaf path with the maximum sum
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path_with_max_sum(root):
    current_sum = 0
    current_path = []  # I want to use this variable as a local => so have to undo what I do
                       # with it inside of function before returning

    # for max_sum and max_path, I have to see the effect of their change outside of function (pass by reference)
    max_sum = [0]  # by reference, so I make it a list
    max_path = []  # when I write max_path = [], it is not working. Because I cannot update it in if statement !!!!

    helper(root, current_path, current_sum, max_path, max_sum)
    return max_path


def helper(current_node, current_path, current_sum, max_path, max_sum):
    if current_node is None:
        return None

    # add the current node to the path
    current_path.append(current_node.val)
    current_sum += current_node.val

    if current_node.left is None and current_node.right is None and current_sum > max_sum[0]:
        max_sum[0] = current_sum
        max_path[:] = current_path  # it is very important to use [:] to copy
        # you cannot write   max_path = currentPath
    else:
        helper(current_node.left, current_path, current_sum, max_path, max_sum)
        helper(current_node.right, current_path, current_sum, max_path, max_sum)

    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack.
    del current_path[-1]  # we should not change the currentPath at each call


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.left.right = TreeNode(8)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(5)
    print("The tree path with maximum sum is: " + str(find_path_with_max_sum(root)))


main()
