'''
Fruits into Baskets

Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal
is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type
of fruit.

You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree
until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Solution: This transforms the current problem into Longest Substring with K Distinct Characters where K=2.
'''


def fruits_into_baskets(fruits):
    window_start = 0
    max_length = 0
    fruit_frequency = {}

    # try to extend the range [window_start, window_end]
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        fruit_frequency[right_fruit] = fruit_frequency.get(right_fruit, 0) + 1

        # shrink the sliding window, until we are left with '2' fruits in the fruit frequency dictionary
        while len(fruit_frequency) > 2:
            left_fruit = fruits[window_start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            window_start += 1  # shrink the window
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
