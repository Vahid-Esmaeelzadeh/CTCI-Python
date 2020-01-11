'''
5205. Unique Number of Occurrences
'''


class Solution:
    def uniqueOccurrences1(self, arr):
        freq = {}
        for i in range(len(arr)):
            freq[arr[i]] = freq.get(arr[i], 0) + 1

        hashset = set()
        for x in freq.values():
            hashset.add(x)

        return len(hashset) == len(freq)

    def uniqueOccurrences(self, arr):
        if len(arr) <= 1:
            return True
        arr.sort()
        occur = []
        count = 1
        i = 0
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                count += 1
            else:
                occur.append(count)
                count = 1

        occur.append(count)

        occur.sort()
        for i in range(len(occur) - 1):
            if occur[i] == occur[i+1]:
                return False

        return True

S = Solution()
arr = [1,2,2,2,1,1]
print(S.uniqueOccurrences1(arr))