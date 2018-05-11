from Message import OnlineMessage
from client.connectClient.ConsoleMenuInput import ConsoleMenuInput
from client.connectClient.ConsoleMenuOutput import ConsoleMenuOutput
from time import sleep
import socket


class ConnectServerClient:

    PAUSE_TIME = 0.1

    MESSAGES_FROM_SERVER = {'AskGame': 'AG',
                            'WrongGame': 'WG',
                            'CorrectGame': 'CG',
                            'JoinGame': 'JG',
                            'TicTacToe': 'TIC'}

    def __init__(self):

        self._sock = None
        self._inputCon = ConsoleMenuInput()
        self._outputCon = ConsoleMenuOutput()
        self._type_game = None

    def connect_server(self):

        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self._sock.connect(('127.0.0.1', 5005))
        except ConnectionRefusedError:
            self._outputCon.cannot_connect_server()
            exit()

        self._sock.settimeout(50)

        self.listen()
        return self._type_game

    def listen(self):

        data = None
        try:
            data = self._sock.recv(512)
            if data == b'':
                self._outputCon.server_close_connection()
                exit()
        except ConnectionAbortedError:
            self._outputCon.breaking_connection_server()
            exit()
        except ConnectionResetError:
            self._outputCon.breaking_connection_server()
            exit()
        except socket.timeout:
            self._outputCon.no_response()
            exit()

        message = OnlineMessage()
        message.decode(data)
        ack = OnlineMessage('ACK')
        self.send(ack)

        self.parse(message)

    def send(self, message):
        try:
            self._sock.send(message.encode())
            sleep(self.PAUSE_TIME)
        except ConnectionResetError:
            self._outputCon.breaking_connection_server()
            exit()

    def get_socket(self):
        return self._sock

    def parse(self, message):

        header = message.get_header()
        data = message.get_body()

        if header == self.MESSAGES_FROM_SERVER['AskGame']:
            self._outputCon.ask_game()
            type_game = self._inputCon.get_game_name()
            message = OnlineMessage(type_game)
            self.send(message)
        elif header == self.MESSAGES_FROM_SERVER['WrongGame']:
            self._outputCon.wrong_game_name()
        elif header == self.MESSAGES_FROM_SERVER['CorrectGame']:
            type_game = data
            if type_game == self.MESSAGES_FROM_SERVER['TicTacToe']:
                self._outputCon.waiting_for_second_player()
            self._type_game = type_game
            return None

        elif header == self.MESSAGES_FROM_SERVER['JoinGame']:
            self._type_game = 'TIC'
            return None

        self.listen()