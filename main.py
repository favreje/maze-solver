# --------------------------------------------------------------------------------------------------
# Name:         Jeffrey Favret
# Date:         1/31/2025
# Project:      Maze-Solver
# Description:  Builds and then solves a maze using tkinter
# --------------------------------------------------------------------------------------------------


from window import Window, Line, Point, Cell


# Testing line drawing ----------------------------------------------------------------------------
def line_test(win):
    lines = (
        Line(Point(10, 10), Point(300, 300)),
        Line(Point(300, 300), Point(300, 400)),
        Line(Point(300, 400), Point(400, 500)),
    )
    for line in lines:
        win.draw_line(line)


# --------------------------------------------------------------------------------------------------


def main():
    win = Window(1040, 1040)

    # line_test(win)

    # Testing cell drawing ------------------------------------------------------------------------

    # Make a 20 x 20 matrix with line length of 50 pixels
    dimensions = []
    for x in range(20, 1000, 50):
        for y in range(20, 1000, 50):
            dimensions.append((Point(x, y), Point(x + 50, y + 50)))
    print(len(dimensions))

    cells = []
    for dim in dimensions:
        cell = Cell(win)
        cell._x1, cell._y1 = dim[0].x, dim[0].y
        cell._x2, cell._y2 = dim[1].x, dim[1].y
        cells.append(cell)

    for cell in cells:
        cell.draw(cell._x1, cell._y1, cell._x2, cell._y2)
    # ----------------------------------------------------------------------------------------------

    win.wait_for_close()


if __name__ == "__main__":
    main()
