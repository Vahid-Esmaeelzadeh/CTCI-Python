'''
1233. Remove Sub-Folders from the Filesystem
'''

class Solution:
    def removeSubfolders(self, folder: list):
        folder.sort()
        n = len(folder)
        i, j = 0, 1
        res = [folder[i]]
        while j < n:
            str1, str2 = folder[i], folder[j]
            if str2[:len(str1)] == str1 and str2[len(str1)] == "/":
                j += 1
            else:
                res.append(folder[j])
                i = j
                j = i + 1
        return res


sol = Solution()
folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
folder1 = ["/a","/a/b/c","/a/b/d"]
folder2 = ["/a/b/c","/a/b/ca","/a/b/d"]


print(sol.removeSubfolders(folder))
print(sol.removeSubfolders(folder1))
print(sol.removeSubfolders(folder2))