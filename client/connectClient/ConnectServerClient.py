from Message import OnlineMessage
from client.connectClient.ConsoleMenuInput import ConsoleMenuInput
from client.connectClient.ConsoleMenuOutput import ConsoleMenuOutput
from time import sleep
import socket


class ConnectServerClient:

    PAUSE_TIME = 0.1

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
        except ConnectionResetError:
            self._outputCon.breaking_connection_server()
            exit()
        except socket.timeout:
            self._outputCon.no_response()
            exit()

        message = OnlineMessage()
        message.decode(data)
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

        if header == 'AG':
            self._outputCon.ask_game()
            type_game = self._inputCon.get_game_name()
            message = OnlineMessage(type_game)
            self.send(message)
        elif header == 'WG':
            self._outputCon.wrong_game_name()
        elif header == 'CG':
            type_game = data
            if type_game == 'TIC':
                self._outputCon.waiting_for_second_player()
            self._type_game = type_game
            return None

        elif header == 'JG':
            self._type_game = 'TIC'
            return None

        self.listen()