# --------------------------------------------------------------------------------------------------
# Name:         Jeffrey Favret
# Date:         1/31/2025
# Project:      Maze-Solver
# Description:  Builds and then solves a maze using tkinter
# --------------------------------------------------------------------------------------------------


from window import Window, Line, Point


def main():
    win = Window(800, 600)

    # Testing line drawing ------------------------------------------------------------------------
    lines = (
        Line(Point(10, 10), Point(300, 300)),
        Line(Point(300, 300), Point(300, 1000)),
        Line(Point(300, 1000), Point(800, 1000)),
    )
    for line in lines:
        win.draw_line(line)
    # ----------------------------------------------------------------------------------------------

    win.wait_for_close()


if __name__ == "__main__":
    main()
