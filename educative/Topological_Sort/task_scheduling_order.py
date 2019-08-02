'''
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed
before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to find
the ordering of tasks we should pick to finish all tasks.
'''

from collections import deque


def find_order(tasks, prerequisites):
    sorted_order = []
    if tasks <= 0:
        return sorted_order

    in_degree, graph = build_graph(tasks, prerequisites)

    # extract sources
    sources = deque()
    for task in in_degree:
        if in_degree[task] == 0:
            sources.append(task)

    # calculate the order
    while sources:
        task = sources.popleft()
        sorted_order.append(task)

        for child_task in graph[task]:
            in_degree[child_task] -= 1
            if in_degree[child_task] == 0:
                sources.append(child_task)

    if len(sorted_order) != tasks:
        return []

    return sorted_order


def build_graph(tasks, prerequisites):
    graph = {i: [] for i in range(tasks)}
    in_degree = {i: 0 for i in range(tasks)}

    for parent_task, task in prerequisites:
        graph[parent_task].append(task)
        in_degree[task] += 1

    return [in_degree, graph]


def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()
