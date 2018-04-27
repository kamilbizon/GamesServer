from client.morelessClient.ConsoleMoreLessInput import ConsoleMoreLessInput
from client.morelessClient.ConsoleMoreLessOutput import ConsoleMoreLessOutput
from Message import OnlineMessage
from time import sleep


class MoreLessClient:

    MESSAGES_FROM_SERVER = {'Welcome': 'WE',
                            'AskMinRange': 'AMI',
                            'GetMinRange': 'GMI',
                            'WrongMinRange': 'WMI',
                            'AskMaxRange': 'AMX',
                            'GetMaxRange': 'GMX',
                            'WrongMaxRange': 'WMX',
                            'AskPlayerGuess': 'APG',
                            'GetGuess': 'GG',
                            'WrongGuess': 'WG',
                            'Less': 'LS',
                            'More': 'MR',
                            'CongratulateWin': 'CW'}

    PAUSE_TIME = 0.1

    def __init__(self, sock):
        self._inputCon = ConsoleMoreLessInput()
        self._outputCon = ConsoleMoreLessOutput()
        self.sock = sock
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

        if header == self.MESSAGES_FROM_SERVER['Welcome']:
            self._outputCon.welcome()
        elif header == self.MESSAGES_FROM_SERVER['AskMinRange']:
            self._outputCon.ask_min_range()
        elif header == self.MESSAGES_FROM_SERVER['GetMinRange']:
            min_range = self._inputCon.get_min_range()
            message = OnlineMessage('', min_range)
            self.send(message)
        elif header == self.MESSAGES_FROM_SERVER['WrongMinRange']:
            self._outputCon.wrong_min_range()
        elif header == self.MESSAGES_FROM_SERVER['AskMaxRange']:
            self._outputCon.ask_max_range()
        elif header == self.MESSAGES_FROM_SERVER['GetMaxRange']:
            min_range = data
            max_range = self._inputCon.get_max_range(min_range)
            message = OnlineMessage('', max_range)
            self.send(message)
        elif header == self.MESSAGES_FROM_SERVER['WrongMaxRange']:
            min_range = data
            self._outputCon.wrong_max_range(min_range)
        elif header == self.MESSAGES_FROM_SERVER['AskPlayerGuess']:
            self._outputCon.ask_player_guess()
        elif header == self.MESSAGES_FROM_SERVER['GetGuess']:
            min_range, max_range = data[0], data[1]
            guess = self._inputCon.get_guess(min_range, max_range)
            message = OnlineMessage('', guess)
            self.send(message)
        elif header == self.MESSAGES_FROM_SERVER['WrongGuess']:
            min_range, max_range = data[0], data[1]
            self._outputCon.wrong_guess(min_range, max_range)
        elif header == self.MESSAGES_FROM_SERVER['Less']:
            self._outputCon.less()
        elif header == self.MESSAGES_FROM_SERVER['More']:
            self._outputCon.more()
        elif header == self.MESSAGES_FROM_SERVER['CongratulateWin']:
            self._outputCon.congratulate_win()
            self.sock.close()
            exit()

        self.listen()