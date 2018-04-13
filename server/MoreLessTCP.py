from time import sleep
from TicTacToeInput import Input
from MoreLessOutput import MoreLessOutput
from server.Server import Server
from Message import OnlineMessage


class MoreLessTCP(Input, MoreLessOutput):

    def __init__(self, server):
        self._server = server
        self._player_list = self._server.get_player_list()

    def change_conn(self):
        if self._conn == self._player_list[0].conn:
            self._conn = self._player_list[1].conn
        else:
            self._conn = self._player_list[0].conn

    def get_player_move(self, dim, player):
        message = OnlineMessage('GM')
        self._server.sent(message.encode())
        message = message.decode(self._server.get())

    def welcome(self):
        message = OnlineMessage('WE')
        self._player_list[1].conn.sendall(message.encode())
        self._player_list[0].conn.sendall(message.encode())
        sleep(0.1)

    def congratulate_winner(self, winner):
        message = OnlineMessage('WE', winner)
        self._conn.sendall(message.encode())
        self._player_list[1].conn.close()
        self._player_list[0].conn.close()

    def announce_draw(self):
        message = OnlineMessage('DR')
        self._conn.sendall(message.encode())
        self._player_list[1].conn.close()
        self._player_list[0].conn.close()

    def get_min_range(self):
        message = OnlineMessage('GMI')
        self._player_list[0].conn.sendall(message.encode())
        self._player_list[1].conn.sendall(message.encode())
        received_message = message.decode(self._server.get())

    def get_max_range(self):
        message = OnlineMessage('GMA')
        self._player_list[0].conn.sendall(message.encode())
        self._player_list[1].conn.sendall(message.encode())
        received_message = message.decode(self._server.get())

    def get_guess(self):
        message = OnlineMessage('GG')
        self._player_list[0].conn.sendall(message.encode())
        self._player_list[1].conn.sendall(message.encode())
        received_message = message.decode(self._server.get())

    def bad_guess(self):
        message = OnlineMessage('BG')

    def less(self):
        pass

    def more(self):
        pass

    def wrong_move(self):
        pass
