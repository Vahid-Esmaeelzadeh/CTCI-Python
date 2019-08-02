class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def find_employee_free_time(schedule):

    free_times = []
    min_times = []
    max_times = []

    for x in schedule:
        free_time = []
        min_time = x[0].start
        max_time = x[0].end

        for i in range(1, len(x)):
            max_time = max(max_time, x[i].end)
            min_time = min(min_time, x[i].start)
            if x[i-1].end < x[i].start:
                free_time.append(Interval(x[i-1].end, x[i].start))

        max_times.append(max_time)
        min_times.append(min_time)
        free_times.append(free_time)



def main():
    input = [[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
