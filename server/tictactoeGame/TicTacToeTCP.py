from tictactoeInputOutputInterface.TicTacToeInput import TicTacToeInput
from tictactoeInputOutputInterface.TicTacToeOutput import TicTacToeOutput
from Message import OnlineMessage


class TicTacToeTCP(TicTacToeInput, TicTacToeOutput):

    MESSAGES_TO_PLAYER = {'YouFirst': 'FI',
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

    def __init__(self, server):
        self._server = server
        self._player_list = self._server.get_player_list()

    def actual_player(self, player):
        if player == 'O':
            return self._player_list[0]
        else:
            return self._player_list[1]

    def first_second(self, player1, player2):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['YouFirst'], player1)
        self._server.send(message.encode(), self.actual_player(player1))
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['YouSecond'], player2)
        self._server.send(message.encode(), self.actual_player(player2))

    def welcome(self):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['Welcome'])
        self._server.send(message.encode(), self._player_list[0])
        self._server.send(message.encode(), self._player_list[1])

    def draw_board(self, board, dim):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['DrawBoard'], board)
        self._server.send(message.encode(), self._player_list[0])
        self._server.send(message.encode(), self._player_list[1])

    def player_move(self, player):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['PlayerMove'], player)
        self._server.send(message.encode(), self._player_list[0])
        self._server.send(message.encode(), self._player_list[1])

    def ask_coord(self, coord, player):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['AskCoord'], coord)
        self._server.send(message.encode(), self.actual_player(player))

    def get_coord(self, dim, player):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['GetCoord'])
        self._server.send(message.encode(), self.actual_player(player))
        message.decode(self._server.get(self.actual_player(player)))
        try:
            coord = int(message.get_body())
        except ValueError:
            return False

        if 1 <= coord <= dim:
            return coord

        return False

    def wrong_coord(self, dim, player):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['WrongCoord'], dim)
        self._server.send(message.encode(), self.actual_player(player))

    def wrong_move(self, player):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['WrongMove'])
        self._server.send(message.encode(), self.actual_player(player))

    def congratulate_winner(self, winner):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['CongratulateWinner'], winner)
        self._server.send(message.encode(), self._player_list[0])
        self._server.send(message.encode(), self._player_list[1])

    def announce_draw(self):
        message = OnlineMessage(self.MESSAGES_TO_PLAYER['AnnounceDraw'])
        self._server.send(message.encode(), self._player_list[0])
        self._server.send(message.encode(), self._player_list[1])

    # NO NEED FOR LARGER BOARD NOW
    #
    # def ask_board_size(self, player):
    #     message = OnlineMessage('AS')
    #     self._server.send(message.encode(), self.actual_player(player))
    #
    # def get_board_size(self, player):
    #     message = OnlineMessage('GS')
    #     self._server.send(message.encode(), self.actual_player(player))
    #     message.decode(self._server.get(self.actual_player(player)))
    #
    #     try:
    #         size = int(message.get_body())
    #     except ValueError:
    #         return False
    #
    #     if size >= 3:
    #         return size
    #
    #     return False
    #
    # def wrong_size(self, player):
    #     message = OnlineMessage('WS')
    #     self._server.send(message.encode(), self.actual_player(player))