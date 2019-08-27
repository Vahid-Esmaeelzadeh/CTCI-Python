'''
Welcome to Facebook!

This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you would like to use for your interview,
simply choose it from the dropdown in the top bar.

Enjoy your interview!

// Find the possible time slots to schedule a meeting
// Input:
//  (1) A time range for the meeting to happen
//  (2) A list of time slots that some of my attendees are busy
// Output:
//  a list of time slots that are possible to schedule the meeting.
//
// Example:
//    busy1
//   |-----|busy2                   busy3
//   |  |--|-----|                 |-----|
//   |  |  |     |                 |     |
// --------------------------------------------------------
//   8  9 10     12:30             14    15      18
//      |-----------------------------------------|
//         time range we want the meeting scheduled
//
// In the example above, the answer should be 12:30 -> 14, and 15 -> 18
'''

# [[8 12:30],   [13, 13:30], [14,15]]
# duration = [9 18]


def find_available_slots(dur, timeslots):
    # merge time slots
    timeslots.sort(key=lambda x: x[0])

    merged_intervals = []

    start = timeslots[0][0]
    end = timeslots[0][1]

    for i in range(1, len(timeslots)):
        slot_start = timeslots[i][0]
        slot_end = timeslots[i][1]

        if slot_start <= end:
            end = max(end, slot_end)
        else:
            merged_intervals.append([start, end])
            start = slot_start
            end = slot_end

    merged_intervals.append([start, end])
    # [[8 12:30], [13: 13:30], [14,15]]

    # [12:30 18]
    # [12:30, 13], [13:30, 18]
    # [12:30, 13], [13:30, 14], [15, 18]

    available_slots = []
    for i in range(len(merged_intervals) - 1):
        available_slots.append([merged_intervals[i][1], merged_intervals[i + 1][0]])

    result = []
    for i in range(len(available_slots)):
        result.append([max(available_slots[i][0], dur[0]), min(available_slots[i][1], dur[1])])

    return result







