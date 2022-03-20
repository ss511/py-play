"""
Given a 2D screen, location of a pixel in the screen and a color,
replace color of the given pixel and all adjacent same colored pixels with the given color.
Example
Input:
screen[M][N] = {{1, 1, 1, 1, 1, 1, 1, 1},
               {1, 1, 1, 1, 1, 1, 0, 0},
               {1, 0, 0, 1, 1, 0, 1, 1},
               {1, 2, 2, 2, 2, 0, 1, 0},
               {1, 1, 1, 2, 2, 0, 1, 0},
               {1, 1, 1, 2, 2, 2, 2, 0},
               {1, 1, 1, 1, 1, 2, 1, 1},
               {1, 1, 1, 1, 1, 2, 2, 1},
               };
    x = 4, y = 4, newColor = 3
The values in the given 2D screen
  indicate colors of the pixels.
x and y are coordinates of the brush,
   newColor is the color that
should replace the previous color on
   screen[x][y] and all surrounding
pixels with same color.

Output:
Screen should be changed to following.
screen[M][N] = {{1, 1, 1, 1, 1, 1, 1, 1},
               {1, 1, 1, 1, 1, 1, 0, 0},
               {1, 0, 0, 1, 1, 0, 1, 1},
               {1, 3, 3, 3, 3, 0, 1, 0},
               {1, 1, 1, 3, 3, 0, 1, 0},
               {1, 1, 1, 3, 3, 3, 3, 0},
               {1, 1, 1, 1, 1, 3, 1, 1},
               {1, 1, 1, 1, 1, 3, 3, 1},
               };
"""


def paint_fill(paint_matrix, x, y, prev_color, new_color):
    if x < 0 or x >= m or y < 0 or y >= n or paint_matrix[x][y] != prev_color or paint_matrix[x][y] == new_color:
        return

    paint_matrix[x][y] = new_color

    paint_fill(paint_matrix, x - 1, y, prev_color, new_color)
    paint_fill(paint_matrix, x + 1, y, prev_color, new_color)
    paint_fill(paint_matrix, x, y - 1, prev_color, new_color)
    paint_fill(paint_matrix, x, y + 1, prev_color, new_color)


if __name__ == "__main__":
    paint1 = [[1, 1, 1, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 1, 0, 0],
             [1, 0, 0, 1, 1, 0, 1, 1],
             [1, 2, 2, 2, 2, 0, 1, 0],
             [1, 1, 1, 2, 2, 0, 1, 0],
             [1, 1, 1, 2, 2, 2, 2, 0],
             [1, 1, 1, 1, 1, 2, 1, 1],
             [1, 1, 1, 1, 1, 2, 2, 1],
             ]
    m, n = 8, 8
    x, y = 4, 4
    p_color = paint1[x][y]
    paint_fill(paint1, x, y, p_color, 3)
    print(paint1)

    paint2 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    m, n = 5, 5
    x, y = 2, 2
    p_color = paint2[x][y]
    paint_fill(paint2, x, y, p_color, 3)
    print(paint2)
