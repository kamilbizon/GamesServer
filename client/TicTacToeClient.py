from client.ConsoleTicTacToeInput import ConsoleTicTacToeInput
from client.ConsoleTicTacToeOutput import ConsoleTicTacToeOutput
from Message import OnlineMessage
import socket

dim = 3


class TicTacToeClient:
    def __init__(self, socket):
        self._inputCon = ConsoleTicTacToeInput()
        self._outputCon = ConsoleTicTacToeOutput()
        self.sock = socket
        self.listen()

    def listen(self):

        data = None
        try:
            while data is None:
                data = self.sock.recv(512)
        except:
            pass

        message = OnlineMessage()
        message.decode(data)
        self.parse(message)

    def parse(self, message):

        header = message.get_header()
        data = message.get_body()

        if header == 'FI':
            self._outputCon.first(data)
        elif header == 'SC':
            self._outputCon.second(data)
        elif header == 'WE':
            self._outputCon.welcome()
        elif header == 'DB':
            board = data
            self._outputCon.draw_board(board)
        elif header == 'GM':
            coord = self._inputCon.get_player_move(dim)
            message = OnlineMessage('', coord)
            self.sock.send(message.encode())
        elif header == 'PM':
            self._outputCon.player_move(data)
        elif header == 'GC':
            self._outputCon.get_coord(data)
        elif header == 'WC':
            self._outputCon.wrong_coord(dim, data)
        elif header == 'WM':
            self._outputCon.wrong_move()
        elif header == 'CW':
            self._outputCon.congratulate_winner(data)
            self.sock.close()
            exit()
        elif header == 'DR':
            self._outputCon.announce_draw()
            self.sock.close()
            exit()

        self.listen()

        # elif header == 'GS':
        #     size = self._inputCon.get_board_size()
        #     self.s.send(bytes(size, 'utf-8'))

        # elif header == 'WS':
        #     self._outputCon.wrong_size()