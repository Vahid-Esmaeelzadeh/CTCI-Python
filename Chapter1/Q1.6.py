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