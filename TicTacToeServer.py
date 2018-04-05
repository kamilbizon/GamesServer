from TicTacToeBoard import TicTacToeBoard
from ConsoleOutput import ConsoleOutput
from ConsoleInput import ConsoleInput
from random import choice
from TicTacToePlayers import TicTacToePlayers
import socket
import json
import time

class server:

    def __init__(self):
        self.TCP_IP = '127.0.0.1'
        self.TCP_PORT = 5005
        BUFFER_SIZE = 512
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.TCP_IP, self.TCP_PORT))

        s.listen(1)
        self.player_list = []

        while len(self.player_list) < 2:
            self.conn, addr = s.accept()
            self.player_list.append(TicTacToePlayers(addr, self.TCP_PORT, 'Player' + str(len(self.player_list)), self.conn))
            data = self.conn.recv(BUFFER_SIZE)
            print(addr, self.conn, json.loads(data.decode("utf-8")))
        self.conn, addr = s.accept()
        while True:
            self.conn.sendall(b'siema')
            time.sleep(1)

