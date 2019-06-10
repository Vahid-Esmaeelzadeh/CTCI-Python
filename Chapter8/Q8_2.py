# Question 8.2 (Robot in a grid)

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
# endregion