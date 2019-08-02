'''
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string.You can assume the string has only uppercase and lowercase letters (a - z).
'''


def compress(s: str):
    if calcLenCompressed(s) > len(s):
        return s

    count = 0
    compressedStr = ""
    for i in range(len(s)):
        count += 1
        if (i + 1 == len(s)) or (s[i] != s[i + 1]):
            compressedStr += s[i] + str(count)
            count = 0

    return compressedStr


def calcLenCompressed(s: str) -> int:
    length = 0
    count = 0
    for i in range(len(s)):
        count += 1
        if (i + 1 == len(s)) or (s[i] != s[i + 1]):
            length += 1 + len(str(count))
            count = 0
    return length

print(compress("aaaaaaaaaaaaaaaaaaaabcccccccccccddddddddddddddddddd"))