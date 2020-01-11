'''
1209. Remove All Adjacent Duplicates in String II
'''


class Solution:
    def removeDuplicates1(self, s, k):
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)

    def removeDuplicates(self, s: str, k: int) -> str:
        res = ""
        while True:
            res = self.remove_k_duplicates(s, k)
            if res == s:
                return res
            s = res

    def remove_k_duplicates(self, s, k):
        i, j = 0, 0
        res = []

        while j < len(s):
            if s[i] == s[j] and j - i < k:
                j += 1
            else:
                if j - i != k:
                    res += list(s[i:j])
                i = j

        if j - i != k:
            res += list(s[i:j])

        return ''.join(res)


sol = Solution()
s = "deeedbbcccbdaa"
k = 3

print(sol.removeDuplicates1(s, k))