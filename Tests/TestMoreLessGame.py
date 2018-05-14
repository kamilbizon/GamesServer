import unittest
from unittest.mock import Mock
from server.morelessGame.MoreLessGame import MoreLessGame


class TemporaryTCPClass:
    def get_player_list(self):
        pass


def pass_function():
    pass


class TestMoreLessGame(unittest.TestCase):

    def test_set_min_range(self):
        temp = TemporaryTCPClass()
        more_less_game = MoreLessGame(temp)

        class TemporaryClassForSetMinRangeTest:
            first_call = True

            def get_min_range_return_first_wrong_next_correct_value(self):
                if self.first_call:
                    self.first_call = False
                    return None
                else:
                    return 0

        tmp = TemporaryClassForSetMinRangeTest()

        more_less_game._TCP.ask_min_range = pass_function
        more_less_game._TCP.get_min_range = tmp.get_min_range_return_first_wrong_next_correct_value
        more_less_game._TCP.wrong_min_range = Mock()

        more_less_game.set_min_range()
        more_less_game._TCP.wrong_min_range.assert_called_once()
        self.assertEqual(0, more_less_game._min_range)

    def test_set_max_range(self):
        temp = TemporaryTCPClass()
        more_less_game = MoreLessGame(temp)

        class TemporaryClassForSetMaxRangeTest:
            first_call = True

            def get_max_range_return_first_wrong_next_correct_value(self, min_range):
                if self.first_call:
                    self.first_call = False
                    return None
                else:
                    return 10

        tmp = TemporaryClassForSetMaxRangeTest()

        more_less_game._min_range = 0
        more_less_game._TCP.ask_max_range = pass_function
        more_less_game._TCP.get_max_range = tmp.get_max_range_return_first_wrong_next_correct_value
        more_less_game._TCP.wrong_max_range = Mock()

        more_less_game.set_max_range()
        more_less_game._TCP.wrong_max_range.assert_called_once()
        self.assertEqual(10, more_less_game._max_range)

    def test_player_guess_return_false_for_wrong_guess(self):
        temp = TemporaryTCPClass()
        more_less_game = MoreLessGame(temp)

        more_less_game._min_range = 2
        more_less_game._max_range = 10
        more_less_game._num_to_guess = 4

        more_less_game._TCP.more = pass_function
        more_less_game._TCP.less = pass_function

        def get_player_guess_return_wrong_value():
            return 6

        more_less_game.get_player_guess = get_player_guess_return_wrong_value
        self.assertFalse(more_less_game.player_guess())

    def test_player_guess_return_true_for_correct_guess(self):
        temp = TemporaryTCPClass()
        more_less_game = MoreLessGame(temp)

        more_less_game._min_range = 2
        more_less_game._max_range = 10
        more_less_game._num_to_guess = 4

        more_less_game._TCP.congratulate_win = pass_function

        def get_player_guess_return_correct_value():
            return 4

        more_less_game.get_player_guess = get_player_guess_return_correct_value

        self.assertTrue(more_less_game.player_guess())


