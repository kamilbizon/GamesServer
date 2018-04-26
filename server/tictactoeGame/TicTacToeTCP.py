from tictactoeInputOutputInterface.TicTacToeInput import TicTacToeInput
from tictactoeInputOutputInterface.TicTacToeOutput import TicTacToeOutput
from Message import OnlineMessage


class TicTacToeTCP(TicTacToeInput, TicTacToeOutput):

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
        self._server.send(message.encode(), self.actual_player(player1))
        message = OnlineMessage('SC', player2)
        self._server.send(message.encode(), self.actual_player(player2))

    def get_player_move(self, dim, player):
        message = OnlineMessage('GM')
        self._server.send(message.encode(), self.actual_player(player))
        message.decode(self._server.get(self.actual_player(player)))
        try:
            coord = int(message.get_body())
        except ValueError:
            return False

        if 1 <= coord <= dim:
            return coord

        return False

    def get_board_size(self, player):
        message = OnlineMessage('GS')
        self._server.send(message.encode(), self.actual_player(player))
        message.decode(self._server.get(self.actual_player(player)))

        try:
            size = int(message.get_body())
        except ValueError:
            return False

        if size >= 3:
            return size

        return False

    def welcome(self):
        message = OnlineMessage('WE')
        self._server.send(message.encode(), self._player_list[0])
        self._server.send(message.encode(), self._player_list[1])

    def ask_board_size(self, player):
        message = OnlineMessage('AS')
        self._server.send(message.encode(), self.actual_player(player))

    def wrong_size(self, player):
        message = OnlineMessage('WS')
        self._server.send(message.encode(), self.actual_player(player))

    def draw_board(self, board, dim):
        message = OnlineMessage('DB', board)
        self._server.send(message.encode(), self._player_list[0])
        self._server.send(message.encode(), self._player_list[1])

    def player_move(self, player):
        message = OnlineMessage('PM')
        self._server.send(message.encode(), self.actual_player(player))

    def get_coord(self, coord, player):
        message = OnlineMessage('GC', coord)
        self._server.send(message.encode(), self.actual_player(player))

    def wrong_coord(self, dim, player):
        message = OnlineMessage('WC', dim)
        self._server.send(message.encode(), self.actual_player(player))

    def wrong_move(self, player):
        message = OnlineMessage('WM')
        self._server.send(message.encode(), self.actual_player(player))

    def congratulate_winner(self, winner):
        message = OnlineMessage('CW', winner)
        self._server.send(message.encode(), self._player_list[0])
        self._server.send(message.encode(), self._player_list[1])

    def announce_draw(self):
        message = OnlineMessage('DR')
        self._server.send(message.encode(), self._player_list[0])
        self._server.send(message.encode(), self._player_list[1])