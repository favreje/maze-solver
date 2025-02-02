from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{width}x{height}+450+35")
        self.__canvas = Canvas(master=self.__root, height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__is_running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"Start of line: {self.p1}  End of line: {self.p2}"

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fill=fill_color,
            width=2,
        )


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

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        if self.has_right_wall:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        if self.has_top_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)))

    def draw_move(self, to_cell, undo=False):
        pass


def main():
    p1 = Point(42, 69)
    p2 = Point(42, 10)
    l = Line(p1, p2)
    print(l)


if __name__ == "__main__":
    main()
