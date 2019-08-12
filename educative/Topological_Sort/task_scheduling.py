'''
Tasks Scheduling

There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be
completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs,
find out if it is possible to schedule all the tasks.
'''


def is_scheduling_possible(tasks, prerequisites):
    sorted_order = []
    adj_dict = convert_to_adj_dict(tasks, prerequisites)

    while len(adj_dict) > 0:
        root_vertices = extract_root_vertices(adj_dict)

        if len(root_vertices) == 0:
            break

        for x in root_vertices:
            sorted_order.append(x)
            del adj_dict[x]

    if len(sorted_order) < tasks:
        return False
    return True


def convert_to_adj_dict(tasks, edges):
    adj_dict = {}

    for i in range(tasks):
        adj_dict[i] = []

    for v1, v2 in edges:
        adj_dict[v1].append(v2)

    return adj_dict


def extract_root_vertices(adj_dict):
    tasks = set(adj_dict.keys())
    dependent_tasks = set()
    for row in adj_dict:
        for x in adj_dict[row]:
            dependent_tasks.add(x)

    return tasks - dependent_tasks


def main():
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))


main()
