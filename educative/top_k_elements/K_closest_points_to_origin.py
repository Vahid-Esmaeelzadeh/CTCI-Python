'''
'K' closest points to the Origin

Given an array of points in the a 2D plane, find ‘K’ closest points to the origin.
'''

from heapq import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

    def __lt__(self, p):
        return (self.x ** 2 + self.y ** 2) > (p.x ** 2 + p.y ** 2)


def find_closest_points(points, k):
    max_heap = []

    for i in range(k):
        heappush(max_heap, points[i])

    for i in range(k, len(points)):
        if points[i].x ** 2 + points[i].y ** 2 < max_heap[0].x ** 2 + max_heap[0].y ** 2:
            heappop(max_heap)
            heappush(max_heap, points[i])

    return list(max_heap)


def find_closest_points_to_origin(points, k):
    max_heap = []

    for i in range(k):
        x, y = points[i][0], points[i][1]
        heappush(max_heap, [-(x**2 + y**2), [x, y]])

    for i in range(k, len(points)):
        x, y = points[i][0], points[i][1]
        if x**2 + y**2 < -max_heap[0][0]:
            heappop(max_heap)
            heappush(max_heap, [-(x**2 + y**2), [x, y]])

    return list(max_heap)


def main():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    result2 = find_closest_points_to_origin([[1, 3], [3, 4], [2, -1]], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()
    print()
    print("Here are the k points closest the origin: ")
    for point in result2:
        print(point[1])


main()
