def StringCompression1(s):
    res = ''
    letters = [0] * 58 # index of all letters (A-Z, a-z)
    for c in s:
        letters[ord(c) - ord('A')] += 1

    for i in range(len(letters)):
        if len(res) > len(s):
            return s
        if letters[i] > 0:
            res = res + chr(i+ord('A')) + str(letters[i])

    return res
def StringCompression2(s):
    if countCompression(s) >= len(s):
        return s

    compressed = ""
    count_consecutive = 0

    for i in range(len(s)):
        count_consecutive += 1
        if i + 1 >= len(s) or s[i] != s[i+1]:
            compressed = compressed + s[i] + str(count_consecutive)
            count_consecutive = 0

    return compressed
def countCompression(s):
    comp_len = 0
    consecutive_len = 0

    for i in range(len(s)):
        consecutive_len += 1
        if i + 1 >= len(s) or s[i] != s[i+1]:
            comp_len += 1 + len(str(consecutive_len))
            consecutive_len = 0

    return comp_len

print(StringCompression2('ttttta   abccccc'))
