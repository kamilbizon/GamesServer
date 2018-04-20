from server.morelessGame.MoreLessTCP import MoreLessTCP
from random import randrange


class MoreLessGame:
    players = ['0', '1']

    def __init__(self, server):
        self._TCP = MoreLessTCP(server)

    def start_game(self):
        self._TCP.welcome()

        self.min_range = None
        while self.min_range is None:
            self._TCP.ask_min_range()
            self.min_range = self._TCP.get_min_range()
            if self.min_range is None:
                self._TCP.wrong_min_range()

        self.max_range = None
        while self.max_range is None:
            self._TCP.ask_max_range()
            self.max_range = self._TCP.get_max_range(self.min_range)
            if self.max_range is None:
                self._TCP.wrong_max_range(self.min_range)

        self._num_to_guess = randrange(self.min_range, self.max_range + 1)

        is_end = False
        while not is_end:
            is_end = self.player_guess()

    def get_player_guess(self):

        self._TCP.ask_player_guess()
        player_guess = None
        while player_guess is None:
            player_guess = self._TCP.get_guess(self.min_range, self.max_range)
            if player_guess is None:
                self._TCP.wrong_guess(self.min_range, self.max_range)
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
