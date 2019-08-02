def find_averages_of_subarrays(K, arr):
    result = []
    for i in range(len(arr)-K+1):
        result.append(sum(arr[i:i+K]) / K)

    return result


def find_averages_of_subarrays1(K, arr):
    result = []
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= K - 1:
            result.append(window_sum / K)
            window_sum -= arr[window_start]
            window_start += 1

    return result


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find_averages_of_subarrays(5, a))
print(find_averages_of_subarrays1(5, a))
