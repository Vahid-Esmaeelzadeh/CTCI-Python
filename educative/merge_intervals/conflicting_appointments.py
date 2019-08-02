def can_attend_all_appointments(intervals):
    start, end = 0, 1

    for i in range(len(intervals)):
        for j in range(i+1, len(intervals)):
            if intervals[j][start] < intervals[i][start] < intervals[j][end] or \
                 intervals[i][start] < intervals[j][start] < intervals[i][end]:

                return False
    return True


def can_attend_all_appointments2(intervals):
    start, end = 0, 1
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][start] < intervals[i-1][end]:
            return False
    return True



print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
print("Can attend all appointments: " + str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
print("Can attend all appointments: " + str(can_attend_all_appointments([[1, 5], [2, 3], [3, 6]])))
print()
print("Can attend all appointments: " + str(can_attend_all_appointments2([[1, 4], [2, 5], [7, 9]])))
print("Can attend all appointments: " + str(can_attend_all_appointments2([[6, 7], [2, 4], [8, 12]])))
print("Can attend all appointments: " + str(can_attend_all_appointments2([[1, 5], [2, 3], [3, 6]])))



