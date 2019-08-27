'''
Time Planner


input:  slotsA = [[10, 50], [60, 120], [140, 210]]   availabilities of employee A
        slotsB = [[0, 15], [60, 70]]  availabilities  of employee B
        dur = 8
output: [60, 68]

'''


def meeting_planner(slotsA, slotsB, dur):
    i, j = 0, 0

    while i < len(slotsA) and j < len(slotsB):

        start = max(slotsA[i][0], slotsB[j][0])
        end = min(slotsA[i][1], slotsB[j][1])

        if end - start >= dur:
            return [start, start + dur]

        if slotsA[i][1] > slotsB[j][1]:
            j += 1
        else:
            i += 1

    return []
