# Two City Scheduling
import math


def twoCitySchedCost(costs):
    return helper(costs, 0, 0, 0, {})


def helper(costs, i, a_count, b_count, memo):
    if i == len(costs):
        return 0

    if (i, a_count, b_count) in memo:
        return memo[(i, a_count, b_count)]

    c1, c2 = math.inf, math.inf

    if a_count < len(costs) / 2:
        c1 = costs[i][0] + helper(costs, i + 1, a_count + 1, b_count, memo)
    if b_count < len(costs) / 2:
        c2 = costs[i][1] + helper(costs, i + 1, a_count, b_count + 1, memo)

    memo[(i, a_count, b_count)] = min(c1, c2)
    return memo[(i, a_count, b_count)]


print(twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))
