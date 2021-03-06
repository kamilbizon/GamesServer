import unittest
from server.tictactoeGame.TicTacToeBoard import TicTacToeBoard

dim = 3     # you can change this value to check any board size >= 3


class TestTicTacToeBoard(unittest.TestCase):
    def test_set_point_return_false_if_field_is_occupied(self):
        board = TicTacToeBoard(dim)
        board.set_point(0, 0, 'X')
        self.assertFalse(board.set_point(0, 0, "X"))

    def test_set_point_return_true_if_field_is_not_occupied(self):
        board = TicTacToeBoard(dim)
        self.assertTrue(board.set_point(0, 0, "X"))

    def test_is_over_return_true_for_horizontal_win(self):
        board = TicTacToeBoard(dim)
        for i in range(board.get_dim()):
            board.set_point(0, i, 'X')
        self.assertTrue(board.is_over())

    def test_is_over_return_true_for_vertical_win(self):
        board = TicTacToeBoard(dim)
        for i in range(board.get_dim()):
            board.set_point(i, 0, 'X')
        self.assertTrue(board.is_over())

    def test_is_over_return_true_for_first_diagonal1_win(self):
        board = TicTacToeBoard(dim)
        for i in range(board.get_dim()):
            board.set_point(i, i, 'X')
        self.assertTrue(board.is_over())

    def test_is_over_return_true_for_second_diagonal1_win(self):
        board = TicTacToeBoard(dim)
        for i in range(board.get_dim()):
            board.set_point(-i, -i, 'X')
        self.assertTrue(board.is_over())

    def test_is_over_return_false_for_draw(self):
        board = TicTacToeBoard(dim)

        if dim % 2 == 1:
            board.set_point(dim - 1, 0, "O")
            for j in range(1, dim):
                board.set_point(dim - 1, j, "X")

            for i in range(0, dim - 1, 2):
                board.set_point(i, 0, "O")
                board.set_point(i + 1, 0, "X")
                for j in range(1, dim):
                    board.set_point(i, j, "X")
                    board.set_point(i + 1, j, "O")
        else:
            for i in range(0, dim - 1, 2):
                board.set_point(i, 0, "O")
                board.set_point(i + 1, 0, "X")
                for j in range(1, dim):
                    board.set_point(i, j, "X")
                    board.set_point(i + 1, j, "O")
        self.assertFalse(board.is_over())

    def test_is_move_available_return_true_for_board_with_empty_fields(self):
        board = TicTacToeBoard()
        board.set_point(0, 0, 'X')
        self.assertTrue(board.is_move_available())

    def test_is_move_available_return_false_for_board_without_empty_fields(self):
        board = TicTacToeBoard(dim)

        if dim % 2 == 1:
            board.set_point(dim - 1, 0, "O")
            for j in range(1, dim):
                board.set_point(dim - 1, j, "X")

            for i in range(0, dim - 1, 2):
                board.set_point(i, 0, "O")
                board.set_point(i + 1, 0, "X")
                for j in range(1, dim):
                    board.set_point(i, j, "X")
                    board.set_point(i + 1, j, "O")
        elif dim % 2 == 0:
            for i in range(0, dim - 1, 2):
                board.set_point(i, 0, "O")
                board.set_point(i + 1, 0, "X")
                for j in range(1, dim):
                    board.set_point(i, j, "X")
                    board.set_point(i + 1, j, "O")

        self.assertFalse(board.is_move_available())


if __name__ == '__main__':
    unittest.main()
