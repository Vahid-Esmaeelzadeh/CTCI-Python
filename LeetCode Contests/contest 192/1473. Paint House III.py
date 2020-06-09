'''
1473. Paint House III

There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n),
some houses that has been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color.
(For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods  [{1}, {2,2}, {3,3}, {2}, {1,1}]).

Given an array houses, an m * n matrix cost and an integer target where:

houses[i]: is the color of the house i, 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j+1.
Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods,
if not possible return -1.


Example 1:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
Example 2:

Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}].
Cost of paint the first and last house (10 + 1) = 11.
Example 3:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
Output: 5
Example 4:

Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.


Constraints:

m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 10^4
'''

def minCost(houses, cost, target):
    ans = minCost_rec(houses, cost, target, 0, 0, {})
    if ans == float('inf'):
        return -1
    return ans


def minCost_rec(houses, cost, target, i, pre_color, memo):
    H = len(houses)
    C = len(cost[0])

    if i == H:  # we have painted all houses
        if target == 0:
            return 0
        return float('inf')

    if (target, i, pre_color) in memo:
        return memo[(target, i, pre_color)]

    if houses[i] != 0:  # it is already painted

        new_target = target
        if houses[i] != pre_color:
            new_target = target - 1

        memo[(target, i, pre_color)] = minCost_rec(houses, cost, new_target, i + 1, houses[i], memo)
        return memo[(target, i, pre_color)]

    # try all possible colors for houses[i]
    min_cost = float('inf')
    for cur_color in range(1, C + 1):  # C is number of colors we can use

        new_target = target
        if cur_color != pre_color:
            new_target = target - 1

        cur_cost = cost[i][cur_color - 1] + minCost_rec(houses, cost, new_target, i + 1, cur_color, memo)
        min_cost = min(min_cost, cur_cost)

    memo[(target, i, pre_color)] = min_cost
    return min_cost


houses = [0, 1, 0, 0, 1, 2, 0, 0, 2, 1]
cost = [[4, 5, 2, 6],
        [8, 3, 2, 9],
        [6, 7, 3, 1],
        [10, 10, 2, 7],
        [6, 5, 2, 4],
        [4, 4, 3, 9],
        [9, 8, 3, 5],
        [7, 9, 10, 3],
        [8, 5, 9, 10],
        [10, 7, 4, 6]]
m = 10
n = 4
target = 6

print(minCost(houses, cost, target))
