'''
1234. Replace the Substring for Balanced String
'''

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s) // 4
        indices = {'Q': [], 'W': [], 'E': [], 'R': []}
        freq = {}
        deleting_items = {}

        for i in range(len(s)):
            x = s[i]
            freq[x] = freq.get(x, 0) + 1
            indices[x].append(i)

            if freq[x] > n:
                deleting_items[x] = freq[x] - n

        print(deleting_items)
        print(indices)
        # i, j = 0, 0
        # while j <



sol = Solution()
sol.balancedString("EWQREQEQ")