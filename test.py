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
        num_cols = 69
        num_rows = 42
        m = Maze(50, 40, num_rows, num_cols, 50, 50)
        self.assertEqual(len(m._cells[0]), num_rows)
        self.assertEqual(len(m._cells), num_cols)


#

if __name__ == "__main__":
    unittest.main()
