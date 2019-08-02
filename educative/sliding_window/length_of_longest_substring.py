def length_of_longest_substring(arr, k):
    zero_indices = [-1]

    for i in range(len(arr)):
        if arr[i] == 0:
            zero_indices.append(i)

    zero_indices.append(len(arr))

    longest_len = 0
    for i in range(k, len(zero_indices) - 1):
        longest_len = max(longest_len, zero_indices[i + 1] - zero_indices[i - k] - 1)

    return longest_len


print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
