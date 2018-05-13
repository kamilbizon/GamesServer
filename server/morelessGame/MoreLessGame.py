from server.morelessGame.MoreLessTCP import MoreLessTCP
from random import randrange


class MoreLessGame:

    def __init__(self, server):
        self._TCP = MoreLessTCP(server)
        self._min_range = None
        self._max_range = None
        self._num_to_guess = None

    def set_min_range(self):
        while self._min_range is None:
            self._TCP.ask_min_range()
            self._min_range = self._TCP.get_min_range()
            if self._min_range is None:
                self._TCP.wrong_min_range()

    def set_max_range(self):
        while self._max_range is None:
            self._TCP.ask_max_range()
            self._max_range = self._TCP.get_max_range(self._min_range)
            if self._max_range is None:
                self._TCP.wrong_max_range(self._min_range)

    def start_game(self):
        self._TCP.welcome()

        self.set_min_range()
        self.set_max_range()
        self._num_to_guess = randrange(self._min_range, self._max_range + 1)

        is_end = False
        while not is_end:
            is_end = self.player_guess()

    def get_player_guess(self):

        self._TCP.ask_player_guess()
        player_guess = None
        while player_guess is None:
            player_guess = self._TCP.get_guess(self._min_range, self._max_range)
            if player_guess is None:
                self._TCP.wrong_guess(self._min_range, self._max_range)
        return player_guess

    def player_guess(self):

        is_end = False

        player_guess = self.get_player_guess()

        if player_guess < self._num_to_guess:
            self._TCP.more()
        elif player_guess > self._num_to_guess:
            self._TCP.less()
        if player_guess == self._num_to_guess:
            self._TCP.congratulate_win()
            is_end = True

        return is_end
