from server.MoreLessTCP import MoreLessTCP
from random import randrange


class MoreLessGame:
    players = ['0', '1']

    def __init__(self, server):
        self._TCP = MoreLessTCP(server)
        self._player_guess = None
        # self._player_1_guess = None
        self._num_to_guess = None

    def start_game(self):
        self._TCP.welcome()
        self.min = self._TCP.get_min_range()
        self.max = self._TCP.get_max_range(self.min)
        self._num_to_guess = randrange(self.min, self.max + 1)
        is_end = False
        while not is_end:
            is_end = self.player_make_move()

    def player_get_move(self):
        self._player_0_guess = False
        while not self._player_0_guess:
            self._player_0_guess = self._TCP.get_guess(self.min, self.max)
            if self._player_0_guess == False:
                self._TCP.bad_guess()

        self._player_1_guess = False
        while not self._player_1_guess:
            self._player_1_guess = self._TCP.get_guess()
            if self._player_1_guess == False:
                self._TCP.bad_guess()
        return True

    def player_make_move(self):

        is_end = False
        good_move = False
        while not good_move:
            good_move = self.player_get_move()
            if not good_move:
                self._TCP.wrong_move()

        if self._player_0_guess == self._num_to_guess:
            self._TCP.congratulate_winner()
            is_end = True

        if self._player_0_guess == self._num_to_guess:
            self._TCP.congratulate_winner()
            is_end = True

        return is_end
