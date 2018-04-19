from MoreLessInput import MoreLessInput


class ConsoleMoreLessInput(MoreLessInput):

    def get_min_range(self):
        min_range = input()

        try:
            min_range = int(min_range)
        except ValueError:
            return False

        return min_range

    def get_max_range(self, min):
        max_range = input()

        try:
            max_range = int(max_range)
        except ValueError:
            return False

        return max_range

    def get_guess(self, min, max):
        guess = input()

        try:
            guess = int(guess)
        except ValueError:
            return False

        return guess