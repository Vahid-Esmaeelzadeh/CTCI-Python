'''
Next Greater Element

'''


class Solution:
    def nextGreaterElements(self, nums):
        stack = [(nums[0], 0)]
        res = [-1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] <= stack[-1][0]:
                stack.append((nums[i], i))
            else:
                while len(stack) > 0 and nums[i] > stack[-1][0]:
                    num_index = stack.pop()[1]
                    res[num_index] = nums[i]
                stack.append((nums[i], i))
        return res

sol = Solution()
nums = [1, 2, 7, 4, 5]

print(sol.nextGreaterElements(nums))