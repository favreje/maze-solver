import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_various_rows_and_cols(self):
        num_cols = 42
        num_rows = 42
        m = Maze(50, 40, num_rows, num_cols, 50, 50)
        self.assertEqual(len(m._cells[0]), num_rows)
        self.assertEqual(len(m._cells), num_cols)

    def test_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(m._cells[0][0].has_top_wall, False)
        self.assertEqual(m._cells[-1][-1].has_bottom_wall, False)

    def test_reset_visited(self):
        m = Maze(50, 40, 20, 20, 50, 50)
        for i in range(m._num_cols):
            for j in range(m._num_rows):
                self.assertEqual(m._cells[i][j]._visited, False)


if __name__ == "__main__":
    unittest.main()
