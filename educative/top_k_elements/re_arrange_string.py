'''
Rearrange string

Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

Example 1:
Input: "aappp"
Output: "papap"

Explanation: In "papap", none of the repeating characters come next to each other.

Example 2:
Input: "Programming"
Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.

Explanation: None of the repeating characters come next to each other.

Example 3:
Input: "aapa"
Output: ""

Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".
'''

from heapq import *


def rearrange_string(str):
    char_freq_map = {}
    for c in str:
        char_freq_map[c] = char_freq_map.get(c, 0) + 1

    max_heap = []

    for char, freq in char_freq_map.items():
        heappush(max_heap, (-freq, char))

    result = []
    prev_char, prev_freq = None, 0

    while max_heap:
        freq, char = heappop(max_heap)

        if prev_char and -prev_freq > 0:
            heappush(max_heap, (prev_freq, prev_char))
        result.append(char)
        prev_char = char
        prev_freq = freq + 1

    return ''.join(result) if len(result) == len(str) else ""


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("aaaabbbbddc"))
    print("Rearranged string:  " + rearrange_string("aapa"))
    print("Rearranged string:  " + rearrange_string("AAa"))


main()
