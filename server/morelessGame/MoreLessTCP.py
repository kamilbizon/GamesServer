from morelessInputOutputInterface.MoreLessInput import MoreLessInput
from morelessInputOutputInterface.MoreLessOutput import MoreLessOutput
from Message import OnlineMessage


class MoreLessTCP(MoreLessInput, MoreLessOutput):

    MESSAGES_TO_PLAYER = {'Welcome': 'WE',
                          'AskMinRange': 'AMI',
                          'GetMinRange': 'GMI',
                          'WrongMinRange': 'WMI',
                          'AskMaxRange': 'AMX',
                          'GetMaxRange': 'GMX',
                          'WrongMaxRange': 'WMX',
                          'AskPlayerGuess': 'APG',
                          'GetGuess': 'GG',
                          'WrongGuess': 'WG',
                          'Less': 'LS',
                          'More': 'MR',
                          'CongratulateWin': 'CW'}

    def __init__(self, server):
        self._server = server
        self._player_list = self._server.get_player_list()

    def welcome(self):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['Welcome'])
        self._server.send(message.encode(), self._player_list[0])

    def ask_min_range(self):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['AskMinRange'])
        self._server.send(message.encode(), self._player_list[0])

    def get_min_range(self):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['GetMinRange'])
        self._server.send(message.encode(), self._player_list[0])
        message.decode(self._server.get(self._player_list[0]))
        try:
            min_range = int(message.get_body())
        except ValueError:
            return None

        return min_range

    def wrong_min_range(self):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['WrongMinRange'])
        self._server.send(message.encode(), self._player_list[0])

    def ask_max_range(self):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['AskMaxRange'])
        self._server.send(message.encode(), self._player_list[0])

    def get_max_range(self, min_range):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['GetMaxRange'])
        self._server.send(message.encode(), self._player_list[0])
        message.decode(self._server.get(self._player_list[0]))
        try:
            max_range = int(message.get_body())
        except ValueError:
            return None

        if min_range < max_range:
            return max_range

        return None

    def wrong_max_range(self, min_range):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['WrongMaxRange'], min_range)
        self._server.send(message.encode(), self._player_list[0])

    def ask_player_guess(self):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['AskPlayerGuess'])
        self._server.send(message.encode(), self._player_list[0])

    def get_guess(self, min_range, max_range):
        min_max = [min_range, max_range]
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['GetGuess'], min_max)
        self._server.send(message.encode(), self._player_list[0])
        message.decode(self._server.get(self._player_list[0]))

        try:
            guess = int(message.get_body())
        except ValueError:
            return None

        if min_range <= guess <= max_range:
            return guess

        return None

    def wrong_guess(self, min_range, max_range):
        min_max = [min_range, max_range]
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['WrongGuess'], min_max)
        self._server.send(message.encode(), self._player_list[0])

    def less(self):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['Less'])
        self._server.send(message.encode(), self._player_list[0])

    def more(self):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['More'])
        self._server.send(message.encode(), self._player_list[0])

    def congratulate_win(self):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['CongratulateWin'])
        self._server.send(message.encode(), self._player_list[0])