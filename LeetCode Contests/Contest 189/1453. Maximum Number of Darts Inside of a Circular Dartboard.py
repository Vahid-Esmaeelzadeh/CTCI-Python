# 1453. Maximum Number of Darts Inside of a Circular Dartboard


def numPoints(points, r):
    for i in range(len(points)):
        points[i].append(i)

    x_sorted_points = sorted(points, key=lambda p:p[0])
    y_sorted_points = sorted(points, key=lambda p:p[1])

    x_window = find_x_window(x_sorted_points, r)
    y_window = find_y_window(y_sorted_points, r)
    x_window = [-10, 10]
    y_window = [-10, 10]

    result = 0
    center = []
    for x in range(x_window[0], x_window[1] + 1):
        for y in range(y_window[0], y_window[1] + 1):
            count = find_numPoints(points, x, y, r)
            if count > result:
                result = count
                center = [x, y]


    return [result, center]

def find_x_window(sorted_points, r):
    max_count = 0
    x_window = [sorted_points[0][0], sorted_points[-1][0]]
    for win_end in range(sorted_points[0][0] + 2*r, sorted_points[-1][0] + 1):
        win_start = win_end - 2*r
        count = 0
        for p in sorted_points:
            if win_start <= p[0] <= win_end:
                count += 1
            if p[0] > win_end:
                break
        if count > max_count:
            max_count = count
            x_window = [win_start, win_end]
    return x_window


def find_y_window(sorted_points, r):
    max_count = 0
    y_window = [sorted_points[0][1], sorted_points[-1][1]]
    for win_end in range(sorted_points[0][1] + 2*r, sorted_points[-1][1] + 1):
        win_start = win_end - 2*r
        count = 0
        for p in sorted_points:
            if win_start <= p[1] <= win_end:
                count += 1
            if p[1] > win_end:
                break
        if count > max_count:
            max_count = count
            y_window = [win_start, win_end]
    return y_window


def find_numPoints(points, x, y, r):
    count = 0
    for p in points:
        if (p[0] - x)*(p[0] - x) + (p[1] - y)*(p[1] - y) <= r*r:
            count += 1
    return count


points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]]
points1 = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]]
print(numPoints(points1, 2))