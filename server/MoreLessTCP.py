from time import sleep
from MoreLessInput import MoreLessInput
from MoreLessOutput import MoreLessOutput
from server.Server import Server
from Message import OnlineMessage


class MoreLessTCP(MoreLessInput, MoreLessOutput):

    def __init__(self, server):
        self._server = server
        self._player_list = self._server.get_player_list()

    def get_player_move(self):
        message = OnlineMessage('GM')
        self._server.sent(message.encode())

    def welcome(self):
        message = OnlineMessage('WE')
        message = OnlineMessage('WE')
        self._server.sent(message.encode(), self._player_list[0])
        sleep(0.1)

    def congratulate_winner(self, winner):
        message = OnlineMessage('CW', winner)
        self._server.sent(message.encode(), self._player_list[0])
        self._server.close_connection(self._player_list[0])

    def get_min_range(self):
        message = OnlineMessage('GMI')
        self._server.sent(message.encode(), self._player_list[0])
        message.decode(self._server.get(self._player_list[0]))
        try:
            min_range = int(message.get_body())
        except ValueError:
            return False

        return min_range

    def get_max_range(self, min_range):
        message = OnlineMessage('GMA')
        self._server.sent(message.encode(), self._player_list[0])
        message.decode(self._server.get(self._player_list[0]))
        try:
            max_range = int(message.get_body())
        except ValueError:
            return False

        if min_range < max_range:
            return max_range

        return False

    def get_guess(self, min, max):
        message = OnlineMessage('GG')
        self._server.sent(message.encode(), self._player_list[0])
        message.decode(self._server.get(self._player_list[0]))

    def bad_guess(self):
        message = OnlineMessage('BG')

    def less(self):
        message = OnlineMessage('LS')
        self._server.sent(message.encode())

    def more(self):
        message = OnlineMessage('MR')
        self._server.sent(message.encode())

    def wrong_move(self):
        message = OnlineMessage('WM')
        self._server.sent(message.encode())