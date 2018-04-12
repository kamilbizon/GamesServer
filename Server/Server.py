import socket

class Server:
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

        s.close()

    def sent(self, message):
        pass

    def get(self):
        pass

