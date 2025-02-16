# --------------------------------------------------------------------------------------------------
# Name:         Jeffrey Favret
# Date:         1/31/2025
# Project:      Maze-Solver
# Description:  Builds and then solves a maze using tkinter
# --------------------------------------------------------------------------------------------------

from window import Window
from maze import Maze


def main():
    win = Window(1100, 1075)
    m = Maze(50, 40, 20, 20, 50, 50, win)
    m.solve()
    print("The maze has been solved!")
    win.wait_for_close()


if __name__ == "__main__":
    main()
