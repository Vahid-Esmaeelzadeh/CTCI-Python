def target_sum_tabulation(arr, s):
    n = len(arr)
    if n == 0:
        return 0

    min_sum, max_sum = -sum(arr), sum(arr)
    dp = {(n % 2, 0): 1}
    result = 0
    for i in range(n - 1, -1, -1):
        for cur_sum in range(min_sum, max_sum + 1):
            count1 = dp.get(((i + 1) % 2, cur_sum - arr[i]), 0)
            count2 = dp.get(((i + 1) % 2, cur_sum + arr[i]), 0)

            dp[(i % 2, cur_sum)] = count1 + count2
            if i == 0:
                result = max(result, count1 + count2)
    return result
