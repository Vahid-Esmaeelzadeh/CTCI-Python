'''
Paint Fill: Implement the "paint fill" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
fill in the surrounding area until the color changes from the original color.
'''

from collections import deque

# region recursive Solution
def paintFill(canvas, newColor, r, c):
    if r < 0 or c < 0 or r >= len(canvas) or c >= len(canvas[0]):
        return
    paintFillHelper(canvas, newColor, r, c, canvas[r][c])


def paintFillHelper(canvas, newColor, r, c, selectedColor):
    if r < 0 or c < 0 or r >= len(canvas) or c >= len(canvas[0]):
        return
    if canvas[r][c] != selectedColor:
        return

    canvas[r][c] = newColor

    paintFillHelper(canvas, newColor, r + 1, c - 1, selectedColor)
    paintFillHelper(canvas, newColor, r + 1, c, selectedColor)
    paintFillHelper(canvas, newColor, r + 1, c + 1, selectedColor)
    paintFillHelper(canvas, newColor, r, c - 1, selectedColor)
    paintFillHelper(canvas, newColor, r, c + 1, selectedColor)
    paintFillHelper(canvas, newColor, r - 1, c - 1, selectedColor)
    paintFillHelper(canvas, newColor, r - 1, c, selectedColor)
    paintFillHelper(canvas, newColor, r - 1, c + 1, selectedColor)
# endregion


# region iterative solution
def paint_fill_iterative(canvas, new_color, r, c):
    rows = len(canvas)
    cols = len(canvas[0])
    old_color = canvas[r][c]

    if r < 0 or c < 0 or r >= rows or c >= cols:  # out of canvas
        return
    queue = deque()

    visited = [[0 for j in range(cols)] for i in range(rows)]
    queue.append([r, c])
    visited[r][c] = 1

    while len(queue) > 0:
        [row, col] = queue.popleft()
        canvas[row][col] = new_color

        neighbors = [[row-1, col-1],
                     [row-1, col],
                     [row-1, col+1],
                     [row,   col-1],
                     [row,   col+1],
                     [row+1, col-1],
                     [row+1, col],
                     [row+1, col+1]]

        for [n_row, n_col] in neighbors:
            if 0 <= n_row < rows and 0 <= n_col < cols and visited[n_row][n_col] == 0 and canvas[n_row][n_col] == old_color:
                queue.append([n_row, n_col])
                visited[n_row][n_col] = 1


# endregion
canvas1 = [['R', 'R', 'R', 'R', 'R', 'R', 'R'],
          ['R', 'R', 'B', 'B', 'B', 'G', 'G'],
          ['B', 'B', 'G', 'G', 'G', 'R', 'R'],
          ['R', 'G', 'B', 'B', 'R', 'R', 'R'],
          ['B', 'B', 'B', 'R', 'B', 'R', 'G']]

canvas2 = [['R', 'R', 'R', 'R', 'R', 'R', 'R'],
          ['R', 'R', 'B', 'B', 'B', 'G', 'G'],
          ['B', 'B', 'G', 'G', 'G', 'R', 'R'],
          ['R', 'G', 'B', 'B', 'R', 'R', 'R'],
          ['B', 'B', 'B', 'R', 'B', 'R', 'G']]

paintFill(canvas1, 'K', 2, 2)
paint_fill_iterative(canvas2, 'K', 2, 2)
print(canvas1)
print(canvas2)


