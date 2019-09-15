'''
longest increasing subsequence
'''


def find_LIS_length(nums):
    return find_LIS_length_recursive(nums, 0, -1)


def find_LIS_length_recursive(nums, currentIndex, previousIndex):
    if currentIndex == len(nums):
        return 0

    # include nums[currentIndex] if it is larger than the last included number
    c1 = 0
    if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
        c1 = 1 + find_LIS_length_recursive(nums, currentIndex + 1, currentIndex)

    # excluding the number at currentIndex
    c2 = find_LIS_length_recursive(nums, currentIndex + 1, previousIndex)

    return max(c1, c2)


def main():
    print(find_LIS_length([4, 2, 3, 6, 10, 1, 12]))
    print(find_LIS_length([-4, 10, 3, 7, 15]))
    print(find_LIS_length([30, 40, 70, 2, 0, 10, 20, 21, 22, 23]))


main()
