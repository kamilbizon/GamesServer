from server.Players import Players
import socket


class Server:
    def __init__(self):
        self.TCP_IP = '127.0.0.1'
        self.TCP_PORT = 5005
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.TCP_IP, self.TCP_PORT))

        self.sock.listen(2)
        self._player_list = {}

    def connect_player(self):
        number_of_players = len(self._player_list)
        while len(self._player_list) == number_of_players:
            print("wait for client")
            self._conn, addr = self.sock.accept()
            self._player_list[number_of_players + 1] = Players(addr, self.TCP_PORT, 'Player' + str(len(self._player_list)), self._conn)

    def get_player_list(self):
        return list(self._player_list.keys())

    def sent(self, message):
        pass

    def get(self):
        pass

