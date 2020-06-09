# 1456. Maximum Number of Vowels in a Substring of Given Length


def maxVowels(s: str, k: int) -> int:
    n = len(s)
    win_start, win_end = 0, 0

    vowels = {'a', 'o', 'e', 'i', 'u'}
    count = 0
    result = 0

    for win_end in range(n):
        if s[win_end] in vowels:
            count += 1

        if win_end >= k - 1:
            result = max(count, result)
            if s[win_start] in vowels:
                count -= 1
            win_start += 1

    result = max(result, count)
    return result


print(maxVowels("abciiidef", 3))