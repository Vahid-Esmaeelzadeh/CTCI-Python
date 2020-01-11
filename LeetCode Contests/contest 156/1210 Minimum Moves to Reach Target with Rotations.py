'''
1210. Minimum Moves to Reach Target with Rotations
'''

from collections import deque


class Solution:
    def minimumMoves(self, grid) -> int:
        n = len(grid)
        start = ((0, 0), (0, 1))
        end = ((n - 1, n - 2), (n - 1, n - 1))

        queue = deque()
        queue.append([start, 0])
        seen = set()
        seen.add(start)

        while queue:
            current_location, count = queue.popleft()
            if current_location == end:
                return count

            # specify all neighbors
            p1 = current_location[0]
            p2 = current_location[1]
            is_horizontal = (p1[0] == p2[0])

            if is_horizontal:
                all_neighbors = [((p1[0], p1[1] + 1), (p2[0], p2[1] + 1)),  # move right
                                 ((p1[0] + 1, p1[1]), (p2[0] + 1, p2[1]))]  # move down
                if p1[0] + 1 < n and p1[1] + 1 < n and grid[p1[0] + 1][p1[1] + 1] == 0:
                    all_neighbors.append(((p1[0], p1[1]), (p2[0] + 1, p2[1] - 1)))  # rotate clockwise
            else:
                all_neighbors = [((p1[0], p1[1] + 1), (p2[0], p2[1] + 1)),  # move right
                                 ((p1[0] + 1, p1[1]), (p2[0] + 1, p2[1]))]  # move down
                if p1[0] + 1 < n and p1[1] + 1 < n and grid[p1[0] + 1][p1[1] + 1] == 0:
                    all_neighbors.append(((p1[0], p1[1]), (p2[0] - 1, p2[1] + 1)))  # rotate counterclockwise

            for node in all_neighbors:
                p1, p2 = node[0], node[1]
                if node not in seen and 0 <= p1[0] < n and 0 <= p1[1] < n and 0 <= p2[0] < n and 0 <= p2[1] < n and \
                        grid[p1[0]][p1[1]] == 0 and grid[p2[0]][p2[1]] == 0:
                    queue.append([node, count + 1])
                    seen.add(node)

        return -1


grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0]]

grid = [[0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 0]]

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]]

grid = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

sol = Solution()
print(sol.minimumMoves(grid))
