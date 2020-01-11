'''
59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

import math


class Solution:
    def generateMatrix(self, n: int):
        mat = [[0 for _ in range(n)] for _ in range(n)]
        layer_num = math.ceil(n / 2)
        i = 1
        for layer in range(layer_num):
            # [1 2 3] top row
            mat[layer][layer:n-layer] = range(i, i + n - 2 * layer)
            i = i + n - 2 * layer
            # right column
            #      4]
            #      5]
            for r in range(layer + 1, n-layer):
                mat[r][n-1-layer] = i
                i += 1
            # bottom row
            # [7 6
            mat[n-layer-1][layer:n-layer-1] = reversed(range(i, i + n - 2 * layer - 1))
            i = i + n - 2 * layer - 1
            # left column
            # 8
            for r in range(n-layer-2, layer, -1):
                mat[r][layer] = i
                i += 1


        return mat

sol = Solution()
print(sol.generateMatrix(4))