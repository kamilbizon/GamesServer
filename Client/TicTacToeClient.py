from Client.ConsoleInput import ConsoleInput
from Client.ConsoleOutput import ConsoleOutput
import socket
import json

dim = 3

class Client:
    def __init__(self):
        self._inputCon = ConsoleInput()
        self._outputCon = ConsoleOutput()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('127.0.0.1', 5005))
        self.listen()

    def listen(self):
        self.s.settimeout(100)

        data = None
        try:
            while data != b'':
                data = self.s.recv(512)
                self.parse(data)
        except:
            pass

    def send(self):
        pass

    def parse(self, data):

        flag = data.decode('utf-8')[0:2]
        print(flag)

        if flag == 'WE':
            self._outputCon.welcome()
        elif flag == 'DB':
            board = json.loads(data[2:-1])
            self._outputCon.draw_board(board, dim)
        elif flag == 'GM':
            coord = self._inputCon.get_player_move(dim)
            self.s.send(bytes(coord, 'utf-8'))
        elif flag == 'PM':
            player = data.decode('utf-8')[-1]
            self._outputCon.player_move(player)
        elif flag == 'GC':
            coord = data.decode('utf-8')[-1]
            self._outputCon.get_coord(coord)
        elif flag == 'WC':
            player = data.decode('utf-8')[-1]
            self._outputCon.wrong_coord(dim)
        elif flag == 'WM':
            self._outputCon.wrong_move()
        elif flag == 'CW':
            winner = data.decode('utf-8')[-1]
            self._outputCon.congratulate_winner(winner)
        elif flag == 'DR':
            self._outputCon.announce_draw()

        self.listen()

        # elif flag == 'GS':
        #     size = self._inputCon.get_board_size()
        #     self.s.send(bytes(size, 'utf-8'))

        # elif flag == 'WS':
        #     self._outputCon.wrong_size()