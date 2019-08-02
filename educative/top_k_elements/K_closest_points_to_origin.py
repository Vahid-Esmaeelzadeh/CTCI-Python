'''
'K' closest points to the Origin

Given an array of points in the a 2D2D plane, find ‘K’ closest points to the origin.
'''

from heapq import *

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

    def __lt__(self, p):
        return (self.x << 1 + self.y << 1) > (p.x << 1 + p.y << 1)


def find_closest_points(points, k):
    max_heap = []

    for i in range(k):
        heappush(max_heap, points[i])

    for i in range(k, len(points)):
        if (points[i].x << 1 + points[i].y << 1) < (max_heap[0].x << 1 + max_heap[0].y << 1):
            heappop(max_heap)
            heappush(max_heap, points[i])

    return list(max_heap)


def main():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()
