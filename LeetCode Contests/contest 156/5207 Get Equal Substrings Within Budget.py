'''
5207. Get Equal Substrings Within Budget
'''


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = [0 for _ in range(len(s))]

        for i in range(len(s)):
            diff[i] = abs(ord(s[i]) - ord(t[i]))

        return self.longest_subarray(diff, maxCost)

    def longest_subarray(self, arr, total):
        start, end = 0, 0
        s = 0
        max_len = 0
        while end < len(arr):
            if s + arr[end] <= total:
                s += arr[end]
                end += 1
            else:
                max_len = max(max_len, end - start)
                if start == end:
                    start += 1
                    end += 1
                    s = 0
                else:
                    s -= arr[start]
                    start += 1

        max_len = max(max_len, end - start)
        return max_len



S = Solution()
s = "abcd"
t = "bcdf"
cost = 3

s = "abcd"
t = "cdef"
cost = 3

s = "abcd"
t = "abde"
cost = 0

s = "krrgw"
t = "zjxss"
cost = 19


s = "pxezla"
t = "loewbi"
cost = 25

s = "krpgjbjjznpzdfy"
t = "nxargkbydxmsgby"
cost = 14

print(S.equalSubstring(s, t, cost))
