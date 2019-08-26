'''
frequency sort

Given a string, sort it based on the decreasing frequency of its characters.
'''

from heapq import *


def sort_character_by_frequency(str):
    char_freq_map = {}

    for c in str:
        char_freq_map[c] = char_freq_map.get(c, 0) + 1

    max_heap = []
    for c, freq in char_freq_map.items():
        heappush(max_heap, (-freq, c))

    result = []
    sorted_map = sorted(char_freq_map.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    for x in sorted_map:
        freq, char = x[1], x[0]
        result.append(char * freq)

    print(sorted(char_freq_map))

    # while max_heap:
    #     freq, char = heappop(max_heap)
    #     result.append(char * (-freq))
    #
    return ''.join(result)


def main():
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
