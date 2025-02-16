from window import Point, Line


class Cell:
    def __init__(
        self,
        win,
        has_top_wall=True,
        has_right_wall=True,
        has_bottom_wall=True,
        has_left_wall=True,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = 0
        self._y1 = 0
        self._x2 = 0
        self._y2 = 0
        self._win = win
        self._visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        erase_color = "#eae9e8"
        if self.has_left_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)), fill_color=erase_color)
        if self.has_right_wall:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        else:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), fill_color=erase_color)
        if self.has_top_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), fill_color=erase_color)
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), fill_color=erase_color)

    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "grey"
        else:
            fill_color = "red"
        start_mid_x = abs(self._x2 - self._x1) // 2
        start_mid_y = abs(self._y2 - self._y1) // 2
        end_mid_x = abs(to_cell._x2 - to_cell._x1) // 2
        end_mid_y = abs(to_cell._y2 - to_cell._y1) // 2
        start = Point(self._x1 + start_mid_x, self._y1 + start_mid_y)
        end = Point(to_cell._x1 + end_mid_x, to_cell._y1 + end_mid_y)
        self._win.draw_line(Line(start, end), fill_color)
