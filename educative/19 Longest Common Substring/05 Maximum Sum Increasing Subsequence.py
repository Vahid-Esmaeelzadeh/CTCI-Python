'''
Maximum Sum Increasing Subsequence
'''


def find_MSIS(nums):
    return find_MSIS_recursive(nums, 0, -1, 0)


def find_MSIS_recursive(nums, currentIndex, previousIndex, sum):
    if currentIndex == len(nums):
        return sum

    # include nums[currentIndex] if it is larger than the last included number
    s1 = sum
    if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
        s1 = find_MSIS_recursive(nums, currentIndex + 1,
                                 currentIndex, sum + nums[currentIndex])

    # excluding the number at currentIndex
    s2 = find_MSIS_recursive(nums, currentIndex + 1, previousIndex, sum)

    return max(s1, s2)


def find_MSIS_dp(nums):
    dp = {}
    return find_MSIS_recursive_dp(dp, nums, 0, -1, 0)


def find_MSIS_recursive_dp(dp, nums, currentIndex, previousIndex, sum):
    if currentIndex == len(nums):
        return sum

    subProblemKey = str(currentIndex) + "-" + \
                    str(previousIndex) + "-" + str(sum)

    if subProblemKey not in dp:
        # include nums[currentIndex] if it is larger than the last included number
        s1 = sum
        if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
            s1 = find_MSIS_recursive_dp(dp, nums, currentIndex + 1, currentIndex, sum + nums[currentIndex])

        # excluding the number at currentIndex
        s2 = find_MSIS_recursive_dp(dp, nums, currentIndex + 1, previousIndex, sum)
        dp[subProblemKey] = max(s1, s2)

    return dp.get(subProblemKey)


def main():
    print(find_MSIS([4, 1, 2, 6, 10, 1, 12]))
    print(find_MSIS([-4, 10, 3, 7, 15]))
    print()
    print(find_MSIS_dp([4, 1, 2, 6, 10, 1, 12]))
    print(find_MSIS_dp([-4, 10, 3, 7, 15]))

main()
