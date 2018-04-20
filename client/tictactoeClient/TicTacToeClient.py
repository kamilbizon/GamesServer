from client.tictactoeClient.ConsoleTicTacToeInput import ConsoleTicTacToeInput
from client.tictactoeClient.ConsoleTicTacToeOutput import ConsoleTicTacToeOutput
from Message import OnlineMessage
from time import sleep

dim = 3


class TicTacToeClient:

    PAUSE_TIME = 0.1

    def __init__(self, socket):
        self._inputCon = ConsoleTicTacToeInput()
        self._outputCon = ConsoleTicTacToeOutput()
        self.sock = socket
        self.listen()

    def listen(self):

        data = None
        try:
            data = self.sock.recv(512)
            if data == b'':
                print("Server closed connection")
                exit()
        except ConnectionResetError:
            print("Breaking communication with the server")
            exit()

        message = OnlineMessage()
        message.decode(data)
        self.parse(message)

    def send(self, message):
        try:
            self.sock.send(message.encode())
            sleep(self.PAUSE_TIME)
        except ConnectionResetError:
            print("Breaking communication with the server")
            exit()

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
            self.send(message)
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