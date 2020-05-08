'''
knapsack problem
Top-down Dynamic Programming with Memoization
'''


def solve_knapsack(profits, weights, capacity):
    memo = {}
    return knapsack_recursive(profits, weights, capacity, 0, memo)


def knapsack_recursive(profits, weights, capacity, currentIndex, memo):
    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    if (capacity, currentIndex) in memo:
        return memo[(capacity, currentIndex)]
    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_recursive(
            profits, weights, capacity - weights[currentIndex], currentIndex + 1, memo)

    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_recursive(profits, weights, capacity, currentIndex + 1, memo)

    memo[(capacity, currentIndex)] = max(profit1, profit2)

    return max(profit1, profit2)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
