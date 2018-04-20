from morelessInputOutputInterface.MoreLessInput import MoreLessInput
from morelessInputOutputInterface.MoreLessOutput import MoreLessOutput
from Message import OnlineMessage


class MoreLessTCP(MoreLessInput, MoreLessOutput):

    def __init__(self, server):
        self._server = server
        self._player_list = self._server.get_player_list()

    def welcome(self):
        message = OnlineMessage('WE')
        self._server.send(message.encode(), self._player_list[0])

    def ask_min_range(self):
        message = OnlineMessage('AMI')
        self._server.send(message.encode(), self._player_list[0])

    def get_min_range(self):
        message = OnlineMessage('GMI')
        self._server.send(message.encode(), self._player_list[0])
        message.decode(self._server.get(self._player_list[0]))
        try:
            min_range = int(message.get_body())
        except ValueError:
            return None

        return min_range

    def wrong_min_range(self):
        message = OnlineMessage('WMI')
        self._server.send(message.encode(), self._player_list[0])

    def ask_max_range(self):
        message = OnlineMessage('AMX')
        self._server.send(message.encode(), self._player_list[0])

    def get_max_range(self, min_range):
        message = OnlineMessage('GMX')
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
        message = OnlineMessage('WMX', min_range)
        self._server.send(message.encode(), self._player_list[0])

    def ask_player_guess(self):
        message = OnlineMessage('APG')
        self._server.send(message.encode(), self._player_list[0])

    def get_guess(self, min_range, max_range):
        min_max = [min_range, max_range]
        message = OnlineMessage('GG', min_max)
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
        message = OnlineMessage('WG', min_max)
        self._server.send(message.encode(), self._player_list[0])

    def less(self):
        message = OnlineMessage('LS')
        self._server.send(message.encode(), self._player_list[0])

    def more(self):
        message = OnlineMessage('MR')
        self._server.send(message.encode(), self._player_list[0])

    def congratulate_win(self):
        message = OnlineMessage('CW')
        self._server.send(message.encode(), self._player_list[0])
        self._server.close_connection(self._player_list[0])