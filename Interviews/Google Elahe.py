'''
Minimum Cost to Hire K Workers

There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them
according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.

Example 1:
Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.

Example 2:
Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately.
'''

import sys
from heapq import *


# using maxHeap - O(NlogN)
def mincostToHireWorkers2(quality, wage, K):
    workers = [(w / q, q, w) for q, w in zip(quality, wage)]
    workers = sorted(workers)

    ans = float('inf')
    max_heap = []
    sumq = 0
    for ratio, q, w in workers:
        heappush(max_heap, -q)
        sumq += q

        if len(max_heap) > K:
            sumq += heappop(max_heap)

        if len(max_heap) == K:
            ans = min(ans, ratio * sumq)

    return float(ans)


# recursive solution
def mincostToHireWorkers(quality, wage, K):
    n = len(quality)
    # make quality_wage array, and sort it based on wage/quality in descending order
    quality_wage = [(quality[i], wage[i]) for i in range(n)]
    quality_wage.sort(key=lambda x: x[1]/x[0], reverse=True)

    return helper(quality_wage, K, 0, sys.maxsize, 0)


def helper(quality_wage, K, index, ratio, paid):
    if K == 0 and index < len(quality_wage):  # we selected K workers, so we should return the paid money
        return paid

    if index >= len(quality_wage):
        if K > 0:  # we reached to the end of array and we could not select K workers
            return sys.maxsize
        else:
            return paid

    current_worker_wage_limit = quality_wage[index][0] * ratio

    result2 = helper(quality_wage, K, index + 1, ratio, paid)

    if quality_wage[index][1] <= current_worker_wage_limit:  # I can select this worker
        new_paid = 0
        new_ratio = 0
        if ratio >= sys.maxsize:  # this is the first worker that we select
            new_paid = paid + quality_wage[index][1]
            new_ratio = quality_wage[index][1] / quality_wage[index][0]
        else:
            new_paid = paid + quality_wage[index][0] * ratio

        result1 = helper(quality_wage, K - 1, index + 1, new_ratio, new_paid)
        return min(result1, result2)

    return result2


quality = [3, 1, 10, 10, 1]
wage = [4, 8, 2, 2, 7]
print(mincostToHireWorkers2(quality, wage, 3))

print([(q, w) for q, w in zip(quality, wage)])