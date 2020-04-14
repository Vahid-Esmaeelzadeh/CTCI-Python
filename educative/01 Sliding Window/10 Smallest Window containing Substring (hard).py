'''
Smallest Window containing Substring with all characters of a pattern

Given a string and a pattern, find the smallest substring in the given string which has all the
characters of the given pattern.
'''


def find_permutation(str, pattern):
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(str) + 1
    char_frequency = {}

    for chr in pattern:
        char_frequency[chr] = char_frequency.get(chr, 0) + 1

    # try to extend the range [window_start, window_end]
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:  # Count every matching of a character
                matched += 1

        # Shrink the window if we can, finish as soon as we remove a matched character
        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start

            left_char = str[window_start]
            window_start += 1
            if left_char in char_frequency:
                # Note that we could have redundant matching characters, therefore we'll decrement the
                # matched count only when the last occurrence of a matched character is going out of the window
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    if min_length > len(str):
        return ""
    return str[substr_start: substr_start + min_length]


def main():
    print(find_permutation("aaabbbbdec", "aabc"))
    print(find_permutation("abdabca", "abc"))
    print(find_permutation("adcad", "abc"))


main()
