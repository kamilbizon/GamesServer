from Input import Input

class ConsoleInput(Input):

    def get_player_move(self, dim):
        coord = input()

        try:
            coord = int(coord)
        except ValueError:
            return False

        return coord

    def get_board_size(self):
        size = input()

        try:
            size = int(size)
        except ValueError:
            return False

        return size