from time import sleep
from TicTacToeInput import Input
from TicTacToeOutput import TicTacToeOutput
from server import Server
from Message import OnlineMessage


class TicTacToeTCP(Input, TicTacToeOutput):

    def __init__(self, server):
        self._server = server
        self._player_list = self._server.get_player_list()

    def actual_player(self, player):
        if player == 'O':
            return self._player_list[0]
        else:
            return self._player_list[1]

    def first_second(self, player1, player2):
        message = OnlineMessage('FI', player1)
        self._server.sent(message.encode(), self.actual_player(player1))
        message = OnlineMessage('SC', player2)
        self._server.sent(message.encode(), self.actual_player(player2))
        sleep(0.1)

    def get_player_move(self, dim, player):
        message = OnlineMessage('GM')
        self._server.sent(message.encode(), self.actual_player(player))
        message.decode(self._server.get(self.actual_player(player)))
        try:
            coord = message.get_body()
        except ValueError:
            return False

        if 1 <= coord <= dim:
            return coord

        return False

    def get_board_size(self, player):
        message = OnlineMessage('GS')
        self._server.sent(message.encode(), self.actual_player(player))
        message.decode(self._server.get(self.actual_player(player)))

        try:
            size = message.get_body()
        except ValueError:
            return False

        if size >= 3:
            return size

        return False

    def welcome(self):
        message = OnlineMessage('WE')
        self._server.sent(message.encode(), self._player_list[0])
        self._server.sent(message.encode(), self._player_list[1])
        sleep(0.1)

    def ask_board_size(self, player):
        message = OnlineMessage('AS')
        self._server.sent(message.encode(), self.actual_player(player))
        sleep(0.1)

    def wrong_size(self, player):
        message = OnlineMessage('WS')
        self._server.sent(message.encode(), self.actual_player(player))
        sleep(0.1)

    def draw_board(self, board, dim):
        message = OnlineMessage('DB', board)
        self._server.sent(message.encode(), self._player_list[0])
        self._server.sent(message.encode(), self._player_list[1])
        sleep(0.1)

    def player_move(self, player):
        message = OnlineMessage('PM')
        self._server.sent(message.encode(), self.actual_player(player))
        sleep(0.1)

    def get_coord(self, coord, player):
        message = OnlineMessage('GC', coord)
        self._server.sent(message.encode(), self.actual_player(player))
        sleep(0.1)

    def wrong_coord(self, dim, player):
        message = OnlineMessage('WC', dim)
        self._server.sent(message.encode(), self.actual_player(player))
        sleep(0.1)

    def wrong_move(self, player):
        message = OnlineMessage('WM')
        self._server.sent(message.encode(), self.actual_player(player))
        sleep(0.1)

    def congratulate_winner(self, winner):
        message = OnlineMessage('CW', winner)
        self._server.sent(message.encode(), self._player_list[0])
        self._server.sent(message.encode(), self._player_list[1])
        self._server.close_connection(self._player_list[1])
        self._server.close_connection(self._player_list[0])

    def announce_draw(self):
        message = OnlineMessage('DR')
        self._server.sent(message.encode(), self._player_list[0])
        self._server.sent(message.encode(), self._player_list[1])
        self._server.close_connection(self._player_list[1])
        self._server.close_connection(self._player_list[0])
