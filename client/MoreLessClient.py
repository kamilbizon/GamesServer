from client.ConsoleMoreLessInput import ConsoleMoreLessInput
from client.ConsoleMoreLessOutput import ConsoleMoreLessOutput
from Message import OnlineMessage
import socket


class MoreLessClient:
    def __init__(self, sock):
        self._inputCon = ConsoleMoreLessInput()
        self._outputCon = ConsoleMoreLessOutput()
        self.sock = sock
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

        print(header)

        if header == 'WE':
            self._outputCon.welcome()
        elif header == 'AMI':
            self._outputCon.ask_min_range()
        elif header == 'GMI':
            min_range = self._inputCon.get_min_range()
            message = OnlineMessage('', min_range)
            self.sock.send(message.encode())
        elif header == 'AMX':
            self._outputCon.ask_max_range()
        elif header == 'GMX':
            max_range = self._inputCon.get_max_range(data)
            message = OnlineMessage('', max_range)
            self.sock.send(message.encode())
        elif header == 'WMX':
            self._outputCon.wrong_max_range(data)
        elif header == 'APG':
            self._outputCon.ask_player_guess()
        elif header == 'GG':
            guess = self._inputCon.get_guess(data[0], data[1])
            message = OnlineMessage('', guess)
            self.sock.send(message.encode())
        elif header == 'WG':
            min_range = data[0]
            max_range = data[1]
            self._outputCon.wrong_guess(min_range, max_range)
        elif header == 'LS':
            self._outputCon.less()
        elif header == 'MR':
            self._outputCon.more()
        elif header == 'CW':
            self._outputCon.congratulate_win()
            self.sock.close()
            exit()

        self.listen()