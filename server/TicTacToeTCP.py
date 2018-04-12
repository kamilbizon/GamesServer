from time import sleep
from Input import Input
from Output import Output
from server import Server
from Message import OnlineMessage


class TicTacToeTCP(Input, Output):

    def __init__(self, server):
        self._server = server
        self._player_list = self._server.get_player_list()

    def change_conn(self):
        if self._conn == self._player_list[0].conn:
            self._conn = self._player_list[1].conn
        else:
            self._conn = self._player_list[0].conn

    def first_second(self, player1, player2):
        self._player_list[1].conn.sendall(b'FI' + bytes(player1, 'utf-8'))
        self._player_list[0].conn.sendall(b'SC' + bytes(player2, 'utf-8'))
        sleep(0.1)

    def get_player_move(self, dim):
        message = OnlineMessage('GM')
        self._server.sent(message.encode())
        message = message.decode(self._server.get())
        try:
            coord = message[1]
        except ValueError:
            return False

        if 1 <= coord <= dim:
            return coord

        return False

    def get_board_size(self):
        self._conn.sendall(b'GS')

        try:
            size = int(self._conn.recv(512))
        except ValueError:
            return False

        if size >= 3:
            return size

        return False

    def welcome(self):
        self._player_list[1].conn.sendall(b'WE')
        self._player_list[0].conn.sendall(b'WE')
        sleep(0.1)

    def ask_board_size(self):
        self._conn.sendall(b'AS')
        sleep(0.1)

    def wrong_size(self):
        self._conn.sendall(b'WS')
        sleep(0.1)

    def draw_board(self, board, dim):
        self._player_list[1].conn.sendall(b'DB' + bytes(json.dumps(board), 'utf-8') + bytes(str(dim), 'utf-8'))
        self._player_list[0].conn.sendall(b'DB' + bytes(json.dumps(board), 'utf-8') + bytes(str(dim), 'utf-8'))
        # self._conn.sendall(bytes(json.dumps(board), 'utf-8'))# + bytes(dim, 'utf-8'))
        sleep(0.1)

    def player_move(self, player):
        self._conn.sendall(b'PM' + bytes(player, 'utf-8'))
        sleep(0.1)

    def get_coord(self, coord):
        self._conn.sendall(b'GC' + bytes(str(coord), 'utf-8'))
        sleep(0.1)

    def wrong_coord(self, dim):
        self._conn.sendall(b'WC' + bytes(str(dim), 'utf-8'))
        sleep(0.1)

    def wrong_move(self):
        self._conn.sendall(b'WM')
        sleep(0.1)

    def congratulate_winner(self, winner):
        self._conn.sendall(b'CW' + bytes(winner, 'utf-8'))
        self._player_list[1].conn.close()
        self._player_list[0].conn.close()

    def announce_draw(self):
        self._conn.sendall(b'DR')
        self._player_list[1].conn.close()
        self._player_list[0].conn.close()

    def get_min_range(self):
        self._player_list[0].conn.sendall(b'GMI')
        self._player_list[1].conn.sendall(b'GMI')

    def get_max_range(self):
        self._player_list[0].conn.sendall(b'GMA')
        self._player_list[1].conn.sendall(b'GMA')

    def get_guess(self):
        self._player_list[0].conn.sendall(b'GG')
        self._player_list[1].conn.sendall(b'GG')
