from TicTacToeInput import TicTacToeInput


class ConsoleTicTacToeInput(TicTacToeInput):

    def get_player_move(self, dim, player = 0):
        coord = input()

        try:
            coord = int(coord)
        except ValueError:
            return False

        return coord

    def get_board_size(self, player):
        size = input()

        try:
            size = int(size)
        except ValueError:
            return False

        return size