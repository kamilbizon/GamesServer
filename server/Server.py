from server.Players import Players
from Message import OnlineMessage
from server.ServerTransitionFSM import ServerTransitionFSM
from server.ServerTransitionFSM import Event
from server.tictactoeGame.TicTacToeGameOnline import TicTacToeGame
from server.morelessGame.MoreLessOnline import MoreLessGame
from time import sleep
import socket


class Server:

    PAUSE_TIME = 0.1

    MESSAGES_TO_USER = {'AskGame': 'AG',
                        'WrongGame': 'WG',
                        'CorrectGame': 'CG',
                        'JoinGame': 'JG'}

    GAME_LIST = {'ML': Event.PLAYER_CHOOSE_MORE_LESS,
                 'TIC': Event.PLAYER_CHOOSE_TIC_TAC_TOE}

    def __init__(self):
        self._server_FSM = ServerTransitionFSM(self)

        self.TCP_IP = '127.0.0.1'
        self.TCP_PORT = 5005
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.TCP_IP, self.TCP_PORT))

        self._player_list = {}

        self._server_FSM.handle_event(Event.START_PLAY)

    def connect_first_player(self):
        self.connect_player()

        self._server_FSM.handle_event(Event.PLAYER_CONNECTED)

    def connect_second_player(self):
        self.connect_player()
        message = OnlineMessage(self.MESSAGES_TO_USER['JoinGame'])
        players = self.get_player_list()
        self.send(message.encode(), players[1])

        self._server_FSM.handle_event(Event.PLAYER_CONNECTED)

    def connect_player(self):
        self.sock.listen(0)
        number_of_players = len(self._player_list)
        while len(self._player_list) == number_of_players:
            print("wait for client")

            conn, address = self.sock.accept()
            self._player_list["player" + str(number_of_players+1)] =\
                Players(address, 'Player' + str(number_of_players), conn)

    def ask_game(self):
        players = self.get_player_list()

        message = OnlineMessage()
        type_game = None
        while type_game not in self.GAME_LIST:
            message = OnlineMessage(self.MESSAGES_TO_USER['AskGame'])
            self.send(message.encode(), players[0])
            message.decode(self.get(players[0]))
            type_game = message.get_header()

            if type_game not in self.GAME_LIST:
                message.set_header(self.MESSAGES_TO_USER['WrongGame'])
                self.send(message.encode(), players[0])

        message.set_header(self.MESSAGES_TO_USER['CorrectGame'])
        message.set_body(type_game)
        self.send(message.encode(), players[0])

        self._server_FSM.handle_event(self.GAME_LIST[type_game])

    def start_more_less_game(self):
        game = MoreLessGame(self)
        game.start_game()
        self._server_FSM.handle_event(Event.GAME_FINISHED)

    def start_tic_tac_toe_game(self):
        game = TicTacToeGame(self)
        game.start_game()
        self._server_FSM.handle_event(Event.GAME_FINISHED)

    def disconnect_players(self):
        for player in self._player_list.keys():
            self.close_connection(player)
        self._player_list.clear()
        self._server_FSM.handle_event(Event.START_PLAY)

    def close_connection(self, player):
        self._player_list[player].conn.close()

    def get_player_list(self):
        return list(self._player_list.keys())

    def send(self, message, player):
        try:
            self._player_list[player].conn.sendall(message)
            sleep(self.PAUSE_TIME)
        except ConnectionResetError:
            print("Connection terminated")
            for player in self._player_list.keys():
                self.close_connection(player)
            exit()
        except ConnectionAbortedError:
            print("Connection terminated")
            for player in self._player_list.keys():
                self.close_connection(player)
            exit()

    def get(self, player):
        message = None
        try:
            message = self._player_list[player].conn.recv(512)
        except ConnectionResetError:
            print("Connection terminated")
            for player in self._player_list.keys():
                self.close_connection(player)
            exit()
        except ConnectionAbortedError:
            print("Connection terminated")
            for player in self._player_list.keys():
                self.close_connection(player)
            exit()

        return message