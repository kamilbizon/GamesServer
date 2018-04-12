from random import randrange
from server.TicTacToeTCP import Server


class MoreLessGame:
    def __init__(self):
        self._min = 0
        self._max = 0
        self._num_to_guess = 0
        self._server = Server()

    def start_game(self):
        self._server.welcome()
        self._min = self._server.get_min_range()
        self._max = self._server.get_max_range()

        self._num_to_guess = randrange(self._min, self._max + 1)

        is_over = False

        while not is_over:
            first_guess = self._server.get_guess()
            second_guess = self._server.get_guess()
            if first_guess == second_guess:
                is_over = True

        return True
