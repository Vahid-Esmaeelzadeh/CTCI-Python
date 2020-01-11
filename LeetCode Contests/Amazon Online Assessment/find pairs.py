'''
Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id and
the second integer represents a value. Your task is to find an element from a and an element form b such that the sum
of their values is less or equal to target and as close to target as possible. Return a list of ids of selected
elements. If no pair is possible, return an empty list.
'''


class Solution:
    def findPairs(self, a, b, target):
        a.sort(key=lambda x: x[1])
        b.sort(key=lambda x: x[1])
        left, right = 0, len(b) - 1
        ans = []
        curDiff = float('inf')
        while left < len(a) and right >= 0:
            id1, a_val = a[left]
            id2, b_val = b[right]

            if target - a_val - b_val == curDiff:
                ans.append([id1, id2])
            elif a_val + b_val <= target and target - a_val - b_val < curDiff:
                ans.clear()
                ans.append([id1, id2])
                curDiff = target - a_val - b_val

            if a_val + b_val < target:
                left += 1
            else:
                right -= 1
        return ans


a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10

sol = Solution()
print(sol.findPairs(a, b, target))