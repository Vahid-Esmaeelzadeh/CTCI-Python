def intersection(intervals_a, intervals_b):
    result = []
    start, end = 0, 1
    temp_interval = []

    for a in intervals_a:
        for b in intervals_b:
            if b[start] <= a[start] <= b[end] or a[start] <= b[start] <= a[end]:
                temp_interval.append(max(a[start], b[start]))
                temp_interval.append(min(a[end], b[end]))
                result.append(temp_interval)
                temp_interval = []

    return result


print("Intervals Intersection: " + str(intersection([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
print("Intervals Intersection: " + str(intersection([[1, 3], [5, 7], [9, 12]], [[5, 10]])))
