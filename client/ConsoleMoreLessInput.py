from MoreLessInput import MoreLessInput


class ConsoleMoreLessInput(MoreLessInput):

    def get_min_range(self):
        min_range = input()
        return min_range

    def get_max_range(self, min):
        max_range = input()
        return max_range

    def get_guess(self, min, max):
        guess = input()
        return guess