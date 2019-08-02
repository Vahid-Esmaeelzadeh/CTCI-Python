'''
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed
before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to print
all possible ordering of tasks meeting all prerequisites.
'''

from collections import deque
import copy


def print_orders(tasks, prerequisites):
    all_orders = [[]]
    if tasks <= 0:
        return all_orders

    in_degree, graph = build_graph(tasks, prerequisites)

    # extract sources
    sources = []
    for task in in_degree:
        if in_degree[task] == 0:
            sources.append(task)

    # calculate the order
    while sources:
        calculate_all_orders(graph, in_degree, sources, all_orders)

    print(all_orders)


def calculate_all_orders(graph, in_degree, sources, all_orders):
    n = len(sources)
    all = len(all_orders)

    for _ in range(n - 1):
        for i in range(all):
            all_orders.append(copy.deepcopy(all_orders[i]))

    start = 0
    i = 0
    for x in sources:
        while i < start + n - 1:
            all_orders[i].append(x)
            i += 1
        start += n

    for i in range(n):
        source = sources[i]
        del sources[i]

        for child_task in graph[source]:
            in_degree[child_task] -= 1

            if in_degree[child_task] == 0:
                sources.append(child_task)


def build_graph(tasks, prerequisites):
    graph = {i: [] for i in range(tasks)}
    in_degree = {i: 0 for i in range(tasks)}

    for parent_task, task in prerequisites:
        graph[parent_task].append(task)
        in_degree[task] += 1

    return [in_degree, graph]


def main():

    # a = [[1], [2], [3]]
    # n = len(a)
    #
    # for i in range(n):
    #     a.append(copy.deepcopy(a[i]))
    #
    # print(a)
    # sources = [4, 5]
    #
    # start = 0
    # i = 0
    # for x in sources:
    #     while i < start + n:
    #         a[i].append(x)
    #         i += 1
    #     start += n
    #
    # print(a)

    # print("Task Orders: ")
    # print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
