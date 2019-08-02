from heapq import *


def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    max_heap_profit = []
    min_heap_capital = []

    available_capital = initialCapital

    for i in range(len(capital)):
        heappush(min_heap_capital, (capital[i], i))

    for _ in range(numberOfProjects):
        while min_heap_capital and available_capital >= min_heap_capital[0][0]:
            c, i = heappop(min_heap_capital)
            heappush(max_heap_profit, (-profits[i], i))

        if not max_heap_profit:
            break

        available_capital += -heappop(max_heap_profit)[0]

    return available_capital

def main():
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
