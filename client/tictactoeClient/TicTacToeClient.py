from client.tictactoeClient.ConsoleTicTacToeInput import ConsoleTicTacToeInput
from client.tictactoeClient.ConsoleTicTacToeOutput import ConsoleTicTacToeOutput
from Message import OnlineMessage
from sys import exit
from time import sleep
import socket

dim = 3


class TicTacToeClient:

    MESSAGES_FROM_SERVER = {'YouFirst': 'FI',
                          'YouSecond': 'SC',
                          'Welcome': 'WE',
                          'DrawBoard': 'DB',
                          'PlayerMove': 'PM',
                          'AskCoord': 'AC',
                          'GetCoord': 'GC',
                          'WrongCoord': 'WC',
                          'WrongMove': 'WM',
                          'CongratulateWinner': 'CW',
                          'AnnounceDraw': 'DR',
                          # NO NEED FOR LARGER BOARD NOW
                          # 'AskBoardSize': 'AS',
                          # 'GetBoardSize': 'GS',
                          # 'WrongBoardSize': 'WS'
                          }

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
        except socket.timeout:
            print("No response")
            exit()

        message = OnlineMessage()
        message.decode(data)
        ack = OnlineMessage('ACK')
        self.send(ack)

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

        if header == self.MESSAGES_FROM_SERVER['YouFirst']:
            self._outputCon.first(data)
        elif header == self.MESSAGES_FROM_SERVER['YouSecond']:
            self._outputCon.second(data)
        elif header == self.MESSAGES_FROM_SERVER['Welcome']:
            self._outputCon.welcome()
        elif header == self.MESSAGES_FROM_SERVER['DrawBoard']:
            board = data
            self._outputCon.draw_board(board)
        elif header == self.MESSAGES_FROM_SERVER['PlayerMove']:
            self._outputCon.player_move(data)
        elif header == self.MESSAGES_FROM_SERVER['AskCoord']:
            self._outputCon.ask_coord(data)
        elif header == self.MESSAGES_FROM_SERVER['GetCoord']:
            coord = self._inputCon.get_coord(dim)
            message = OnlineMessage('', coord)
            self.send(message)
        elif header == self.MESSAGES_FROM_SERVER['WrongCoord']:
            self._outputCon.wrong_coord(dim, data)
        elif header == self.MESSAGES_FROM_SERVER['WrongMove']:
            self._outputCon.wrong_move()
        elif header == self.MESSAGES_FROM_SERVER['CongratulateWinner']:
            self._outputCon.congratulate_winner(data)
            self.sock.close()
            exit()
        elif header == self.MESSAGES_FROM_SERVER['AnnounceDraw']:
            self._outputCon.announce_draw()
            self.sock.close()
            exit()

        self.listen()

         # NO NEED FOR LARGER BOARD NOW
         # elif header == self.MESSAGES_FROM_SERVER['']:
         #     size = self._inputCon.get_board_size()
         #     self.s.send(bytes(size, 'utf-8'))
         #
         # elif header == 'WS':
         #     self._outputCon.wrong_size()