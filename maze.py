import time
import random
from cell import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):

        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells = []
        self._win = win
        if seed is not None:
            self._seed = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited_cells()

    def _create_cells(self):
        for _ in range(self._num_cols):
            col = []
            for _ in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.055)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[-1][-1]
        entrance.has_top_wall = False
        self._draw_cell(0, 0)
        exit.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        north_col, north_row = (i, j - 1)
        east_col, east_row = (i + 1, j)
        south_col, south_row = (i, j + 1)
        west_col, west_row = (i - 1, j)
        self._cells[i][j]._visited = True

        while True:
            to_visit = []

            if north_col in range(self._num_cols) and north_row in range(self._num_rows):
                north = self._cells[north_col][north_row]
                if not north._visited:
                    to_visit.append((north_col, north_row))
            if east_col in range(self._num_cols) and east_row in range(self._num_rows):
                east = self._cells[east_col][east_row]
                if not east._visited:
                    to_visit.append((east_col, east_row))
            if south_col in range(self._num_cols) and south_row in range(self._num_rows):
                south = self._cells[south_col][south_row]
                if not south._visited:
                    to_visit.append((south_col, south_row))
            if west_col in range(self._num_cols) and west_row in range(self._num_rows):
                west = self._cells[west_col][west_row]
                if not west._visited:
                    to_visit.append((west_col, west_row))
            if not to_visit:
                self._draw_cell(i, j)
                return

            current_cell = self._cells[i][j]
            selected_direction = random.choice(to_visit)
            selected_cell = self._cells[selected_direction[0]][selected_direction[1]]

            if (selected_direction[0], selected_direction[1]) == (north_col, north_row):
                current_cell.has_top_wall = False
                selected_cell.has_bottom_wall = False
                self._draw_cell(i, j)
                self._draw_cell(north_col, north_row)
                self._break_walls_r(north_col, north_row)
            elif (selected_direction[0], selected_direction[1]) == (south_col, south_row):
                current_cell.has_bottom_wall = False
                selected_cell.has_top_wall = False
                self._draw_cell(i, j)
                self._draw_cell(south_col, south_row)
                self._break_walls_r(south_col, south_row)
            elif (selected_direction[0], selected_direction[1]) == (east_col, east_row):
                current_cell.has_right_wall = False
                selected_cell.has_left_wall = False
                self._draw_cell(i, j)
                self._draw_cell(east_col, east_row)
                self._break_walls_r(east_col, east_row)
            elif (selected_direction[0], selected_direction[1]) == (west_col, west_row):
                current_cell.has_left_wall = False
                selected_cell.has_right_wall = False
                self._draw_cell(i, j)
                self._draw_cell(west_col, west_row)
                self._break_walls_r(west_col, west_row)

    def _reset_visited_cells(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j]._visited = False
