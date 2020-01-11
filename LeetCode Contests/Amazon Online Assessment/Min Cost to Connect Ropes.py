'''
Min Cost to Connect Ropes

Given n ropes of different lengths, we need to connect these ropes into one rope. We can connect only 2 ropes at a time.
The cost required to connect 2 ropes is equal to sum of their lengths. The length of this connected rope is also equal
to the sum of their lengths. This process is repeated until n ropes are connected into a single rope.
Find the min possible cost required to connect all ropes.
'''

from heapq import *


def connect_ropes(ropes):
    min_heap = []
    for x in ropes:
        heappush(min_heap, x)

    cost = 0
    while len(min_heap) > 1:
        temp = heappop(min_heap) + heappop(min_heap)
        cost += temp
        heappush(min_heap, temp)

    return cost


ropes = [1, 2, 5, 10, 35, 89]

print(connect_ropes(ropes))