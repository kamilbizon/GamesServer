from time import sleep
from Input import Input
from Output import Output
from Server.TicTacToePlayers import TicTacToePlayers
import socket
import json


class Server(Input, Output):

    def __init__(self):
        self.TCP_IP = '127.0.0.1'
        self.TCP_PORT = 5005
        BUFFER_SIZE = 512
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.TCP_IP, self.TCP_PORT))

        s.listen(2)
        self._player_list = []

        while len(self._player_list) < 2:
            print("wait for client")
            self._conn, addr = s.accept()
            self._player_list.append(TicTacToePlayers(addr, self.TCP_PORT, 'Player' + str(len(self._player_list)), self._conn))
            # data = self._conn.recv(BUFFER_SIZE)
            # print(addr, self._conn, json.loads(data.decode("utf-8")))
        # self._conn, addr = s.accept()
        # while True:
        #     self._conn.sendall(b'siema')
        #     time.sleep(1)
        s.close()

    def first_second(self, player1, player2):
        self._player_list[1].conn.sendall(b'FI' + bytes(player1, 'utf-8'))
        self._player_list[0].conn.sendall(b'SC' + bytes(player2, 'utf-8'))
        sleep(0.1)


    def get_player_move(self, dim):
        self._conn.sendall(b'GM')
        print("kappa")
        try:
            coord = int(self._conn.recv(10))
            print("mleko")
        except ValueError:
            return False

        if 0 < coord < dim:
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
        sleep(0.1)

    def announce_draw(self):
        self._conn.sendall(b'DR')
        sleep(0.1)