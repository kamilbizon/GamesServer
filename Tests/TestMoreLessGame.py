import unittest
from server.morelessGame.MoreLessGame import MoreLessGame


class TemporaryClass:
    def get_player_list(self):
        pass


def pass_function():
    pass


class TestMoreLessGame(unittest.TestCase):

    temp = TemporaryClass()

    more_less_game = MoreLessGame(temp)
    more_less_game._min_range = 0
    more_less_game._max_range = 10
    more_less_game._num_to_guess = 5

    more_less_game._TCP.more = pass_function
    more_less_game._TCP.less = pass_function

    def test_player_guess_return_false_for_wrong_guess(self):

        def get_player_guess_return_wrong_value():
            return 6

        self.more_less_game.get_player_guess = get_player_guess_return_wrong_value

        self.assertFalse(self.more_less_game.player_guess())

    def test_player_guess_return_true_for_correct_guess(self):

        def get_player_guess_return_correct_value():
            return 4

        self.more_less_game.get_player_guess = get_player_guess_return_correct_value

        self.assertFalse(self.more_less_game.player_guess())