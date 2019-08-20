'''
Maximum Trapping Water
Suppose you are given an array containing non-negative numbers representing heights of a set of buildings.
Now, because of differences in heights of buildings water can be trapped between them.
Find the two buildings that will trap the most amount of water. Write a function that will return the maximum volume
of water that will be trapped between these two buildings.

Example 1:

Input: [1, 3, 5, 4, 1]
Output: 6
Explanation: The maximum water will be trapped between buildings of height 3 and 4.
'''


def find_max_water(building_heights):
    # use two pointer approach to find the maximum area
    left, right = 0, len(building_heights) - 1
    max_area, current_area = 0, 0

    while left < right:
        current_area = (right - left) * min(building_heights[left], building_heights[right])

        if building_heights[left] < building_heights[right]:
            left += 1
        else:
            right -= 1

        max_area = max(max_area, current_area)

    return max_area


def main():
    print(find_max_water([1, 3, 5, 4, 1]))
    print(find_max_water([3, 2, 5, 4, 2]))
    print(find_max_water([1, 4, 3, 2, 5, 8, 4]))


main()
