def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # first column
    for i in range(0, n + 1):
        dp[i][0] = 0

    # last row
    for c in range(0, capacity + 1):
        dp[0][c] = 0

    for i in range(n - 1, -1, -1):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0

            if weights[i] <= c:
                profit1 = profits[i] + dp[i + 1][c - weights[i]]

            profit2 = dp[i + 1][c]
            dp[i][c] = max(profit1, profit2)

    print_selected_elements(dp, weights, capacity)
    return dp[0][capacity]


def print_selected_elements(dp, weights, capacity):
    print("Selected items are: ", end='')
    for i in range(len(weights)):
        if dp[i + 1][capacity] != dp[i][capacity]:
            print(str(i) + " ", end='')
            capacity -= weights[i]
    print()


def solve_knapsack_opt(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for _ in range(capacity + 1)] for _ in range(2)]

    # last row
    for c in range(0, capacity + 1):
        dp[0][c] = 0
    dp[1][0] = 0

    for i in range(n - 1, -1, -1):
        for c in range(1, capacity + 1):
            profit1, profit2 = 0, 0

            if weights[i] <= c:
                profit1 = profits[i] + dp[(i + 1) % 2][c - weights[i]]

            profit2 = dp[(i + 1) % 2][c]
            dp[i % 2][c] = max(profit1, profit2)

    return dp[0][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 4))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([4, 5, 3, 7], [2, 3, 1, 4], 5))

    print()

    print(solve_knapsack_opt([1, 6, 10, 16], [1, 2, 3, 5], 4))
    print(solve_knapsack_opt([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack_opt([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_opt([4, 5, 3, 7], [2, 3, 1, 4], 5))
main()
