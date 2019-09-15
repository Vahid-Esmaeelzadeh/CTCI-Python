'''
No-repeat longest Substring
Given a string, find the length of the longest substring which has no repeating characters.
'''


def non_repeat_substring(st):
    charSet = set()
    start, end = 0, 0
    maxLen = 0

    for end in range(len(st)):
        if st[end] not in charSet:
            charSet.add(st[end])
        else:
            while st[start] != st[end]:
                charSet.remove(st[start])
                start += 1
            start += 1

        maxLen = max(maxLen, end - start + 1)

    return maxLen


def main():
    print(non_repeat_substring("aabccbb"))
    print(non_repeat_substring("abbbb"))
    print(non_repeat_substring("abccde"))
    print(non_repeat_substring("abcdefghij"))


main()
