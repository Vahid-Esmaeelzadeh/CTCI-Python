'''
Minimum Deletions to Make a Sequence Sorted
'''


def find_minimum_deletions(nums):
    # subtracting the length of LIS from the length of the input array to get minimum number of deletions
    return len(nums) - find_LIS_length(nums)


def find_LIS_length(nums):
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = 1

    maxLength = 1
    for i in range(1, n):
        dp[i] = 1
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
                maxLength = max(maxLength, dp[i])

    return maxLength


def main():
    print(find_minimum_deletions([4, 2, 3, 6, 10, 1, 12]))
    print(find_minimum_deletions([-4, 10, 3, 7, 15]))
    print(find_minimum_deletions([3, 2, 1, 0]))


main()
