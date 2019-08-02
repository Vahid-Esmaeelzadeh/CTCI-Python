def search_ceiling_of_a_number(arr, key):
    if key > arr[-1]:
        return -1
    if key <= arr[0]:
        return 0

    start, end = 0, len(arr) - 1

    while start <= end:
        # calculate the middle of the current range
        mid = start + (end - start) // 2

        if key == arr[mid]:
            return mid

        if key < arr[mid]:
            end = mid - 1  # the 'key' can be in the first half
        else:  # key > arr[mid]
            start = mid + 1  # the 'key' can be in the second half

    return start


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
