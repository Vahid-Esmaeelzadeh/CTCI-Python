'''
Substrings with exactly K distinct chars

Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly k
distinct characters. If the given string doesn't have k distinct characters, return 0.
'''


def substrings_with_k_distinct_chars(st, k):
    freq = {}  # {char: count}
    start, end = 0, 0

    count = 0

    while end < len(st):
        char = st[end]
        freq[char] = freq.get(char, 0) + 1

        end += 1

        if len(freq) == k:
            count += 1
            print(st[start:end])
            continue

        while len(freq) > k:
            freq[st[start]] -= 1
            if freq[st[start]] == 0:
                del freq[st[start]]

            start += 1

        if len(freq) == k:
            count += 1
            print(st[start:end])

    return count


s = "pqpqs"
k = 2

print(substrings_with_k_distinct_chars(s, k))