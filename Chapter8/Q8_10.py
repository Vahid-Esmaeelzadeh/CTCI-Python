#region Question 8.10 (PaintFill)
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


canvas = [['R', 'R', 'R', 'R', 'R', 'R', 'R'],
          ['R', 'R', 'B', 'B', 'B', 'G', 'G'],
          ['B', 'B', 'G', 'G', 'G', 'R', 'R'],
          ['R', 'G', 'B', 'B', 'R', 'R', 'R'],
          ['B', 'B', 'B', 'R', 'B', 'R', 'G']]

paintFill(canvas, 'K', 2, 2)
print(canvas)
# endregion
