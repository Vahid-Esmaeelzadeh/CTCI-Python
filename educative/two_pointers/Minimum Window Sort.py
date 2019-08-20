'''
Minimum Window Sort

Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
'''


# my solution
def shortest_window_sort(arr):
    min_val = min(arr)
    max_val = max(arr)

    left, right = 0, len(arr) - 1
    left_found = False
    right_found = False

    while left <= right and not(left_found and right_found):
        if not left_found:
            if arr[left] == min_val:
                left += 1
            elif arr[left] > min_val:
                min_val = arr[left]
                left += 1
            else:
                left -= 1
                left_found = True

        if not right_found:
            if arr[right] == max_val:
                right -= 1
            elif arr[right] < max_val:
                max_val = arr[right]
                right -= 1
            else:
                right += 1
                right_found = True

    return arr[left: right+1]


def main():
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))


main()
