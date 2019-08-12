'''
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits"such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.

S 1 1 1 1 1 1
1 1 0 1 1 0 0
1 0 1 1 0 1 1
1 0 0 0 1 1 D

'''




# region Recursive approach
def pathFinder(maze):
    path = []
    if len(maze) == 0:
        return path

    pathFinder_helper(maze, len(maze) - 1, len(maze[0]) - 1, path)
    return path


def pathFinder_helper(maze, r, c, path):
    if (maze[r][c] is False) or r < 0 or c < 0:
        return False

    isOrigin = (r == 0 and c == 0)

    if isOrigin or pathFinder_helper(maze, r, c-1, path) or pathFinder_helper(maze, r-1, c, path):
        path.append((r, c))
        return True

    return False


maze = [[True, True, True, False, True, True, True, True],
        [True, True, True, False, True, True, False, True],
        [True, False, True, True, True, False, False, True],
        [True, False, False, False, True, False, True, True],
        [True, True, True, False, True, True, True, True]]

print(pathFinder(maze))
# endregion


# solve in opposite direction
def robot_in_grid(maze):
    path = []
    if len(maze) == 0:
        return path

    helper(maze, 0, 0, path)
    return path[::-1]


def helper(maze, r, c, path):
    if r >= len(maze) or c >= len(maze[0]) or maze[r][c] is False:
        return False

    if (r == len(maze) - 1 and c == len(maze[0]) - 1) or helper(maze, r+1, c, path) or helper(maze, r, c+1, path):
        path.append((r, c))
        return True

    return False


print(robot_in_grid(maze))
# endregion


# region Dynamic programming approach
def pathFinder_DP(maze):
    if len(maze) == 0:
        return []

    path = []
    failedPoints = set()

    pathFinder_helper_DP(maze, len(maze) - 1, len(maze[0]) - 1, path, failedPoints)
    return path


def pathFinder_helper_DP(maze, r, c, path, failedPoints):
    if (maze[r][c] is False) or r < 0 or c < 0:
        return False

    if (r, c) in failedPoints:
        return False

    isOrigin = (r == 0 and c == 0)

    if isOrigin or pathFinder_helper_DP(maze, r, c-1, path, failedPoints) or pathFinder_helper_DP(maze, r-1, c, path, failedPoints):
        path.append((r, c))
        return True

    failedPoints.add((r, c))  # cache the failed point
    return False

print(pathFinder_DP(maze))
