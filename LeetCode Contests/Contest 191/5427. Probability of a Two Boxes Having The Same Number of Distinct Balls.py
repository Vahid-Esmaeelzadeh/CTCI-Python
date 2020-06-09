# 5427. Probability of a Two Boxes Having The Same Number of Distinct Balls

from collections import deque
import math

def getProbability(balls) -> float:
    balls_list = []
    total, valid = math.inf, 0
    for i in range(len(balls)):
        count = balls[i]
        for _ in range(count):
            balls_list.append(i + 1)

    n = sum(balls_list) / 2

    queue = deque()
    queue.append([0, [], []])

    while queue:
        i, box1, box2 = queue.popleft()

        if i < len(balls_list):
            new_ball = balls_list[i]

            if len(box1) == n and len(box2) == n:
                total += 1
                if isDistinct(box1) and isDistinct(box2):
                    valid += 1
            else:
                if len(box1) < n:
                    for j in range(len(box1) + 1):
                        queue.append([i + 1, box1[0:j] + [new_ball] + box1[j:], box2])
                        if j < len(box1) and new_ball == box1[j]:
                            break

                if len(box2) < n:
                    for j in range(len(box2) + 1):
                        queue.append([i + 1, box1, box2[j:] + [new_ball] + box2[j:]])
                        if j < len(box2) and new_ball == box2[j]:
                            break

    return valid/total


def isDistinct(box):
    s1 = set()
    for x in box:
        s1.add(x)

    return len(s1) == len(box)


print(getProbability([1,2,1,2]))

b = deque()
b.append(1)
b.append(2)
b.append(3)

print(isDistinct(b))