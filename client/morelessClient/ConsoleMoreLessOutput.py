from morelessInputOutputInterface.MoreLessOutput import MoreLessOutput

class ConsoleMoreLessOutput(MoreLessOutput):

    def welcome(self):
        print("Welcome in More/Less game!")

    def ask_min_range(self):
        print("What is the minimum number in the range from which you want to guess?")

    def wrong_min_range(self):
        print("The minimum number must be integer")

    def ask_max_range(self):
        print("What is the maximum number in the range from which you want to guess?")

    def wrong_max_range(self, min_range):
        print("The maximum number must be integer more than ", min_range)

    def ask_player_guess(self):
        print("What's your guess?")

    def less(self):
        print("It's less")

    def more(self):
        print("It's more")

    def wrong_guess(self, min_range, max_range):
        print("Your guess must be integer between ", min_range, " and ", max_range)

    def congratulate_win(self):
        print("Your guess is correct, you win!")