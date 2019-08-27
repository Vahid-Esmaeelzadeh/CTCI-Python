'''
String Permutations with Duplicates: Write a method to compute all permutations of a string whose
characters are not necessarily unique.The list of permutations should not have duplicates.
'''


def permutations_with_dups(str):
    char_count_map = build_freq_table(str)
    return helper(char_count_map)


def helper(char_count_map):
    result = []
    # base case
    remaining_chars_count = 0
    for char in char_count_map:
        remaining_chars_count += char_count_map[char]

    if remaining_chars_count == 0:
        return [""]

    # recursive part
    for char in char_count_map:
        if char_count_map[char] > 0:
            char_count_map[char] -= 1
            lst = helper(char_count_map)
            for s in lst:
                result.append(char + s)
            char_count_map[char] += 1
    return result


def build_freq_table(str):
    freq_table = dict()
    for c in str:
        freq_table[c] = freq_table.get(c, 0) + 1

    return freq_table


freqTable = build_freq_table('baabcdd')
print(freqTable)

print(permutations_with_dups("aaaaab"))

