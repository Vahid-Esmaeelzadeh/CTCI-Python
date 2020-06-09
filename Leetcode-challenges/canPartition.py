from collections import deque


def canPartition(n, dislikes):
    graph = {i: [] for i in range(1, n + 1)}
    for i, j in dislikes:
        graph[i].append(j)
        graph[j].append(i)

    part = [0 for _ in range(n + 1)]
    queue = deque()
    queue.append(1)
    part[1] = 1
    unseen = set(range(1, n + 1))
    unseen.remove(1)

    while queue:
        curPerson = queue.popleft()
        for person in graph[curPerson]:
            if person in unseen:
                part[person] = -part[curPerson]
                queue.append(person)
                unseen.remove(person)
            else:
                if part[person] == part[curPerson]:
                    return False
        if len(queue) == 0 and len(unseen) > 0:
            newPerson = unseen.pop()
            queue.append(newPerson)
            part[newPerson] = 1

    return True




print(canPartition(4, [[1,2],[1,3],[2,4]]))