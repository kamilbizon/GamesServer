from Server.TicTacToeBoard import TicTacToeBoard
from random import sample
from Server.TicTacToeServer import Server


class Game:
    players = ['O', 'X']

    def __init__(self):
        self._server = Server()

        # no need for larger board atm
        # self._server.ask_board_size()
        #
        # dim = False
        # while not dim:
        #     dim = self._server.get_board_size()
        #     if not dim:
        #         self._server.wrong_size()

        self._dim = 3
        self._board = TicTacToeBoard(self._dim)

        players = sample(self.players, 2)
        self._actual_player = players[0]
        second_player = players[1]

        print(self._actual_player, second_player)

        self._server.first_second(self._actual_player, second_player)

    def start_game(self):
        self._server.welcome()
        self._server.draw_board(self._board.get_board_state(), self._dim)

        is_end = False
        while not is_end:
            is_end = self.player_make_move()


    def player_get_move(self):

        self._server.player_move(self._actual_player)
        self._server.get_coord('x')

        x = False
        while not x:
            x = self._server.get_player_move(self._dim)
            if x == False:
                self._server.wrong_coord(self._dim)

        self._server.get_coord('y')
        y = False
        while not y:
            y = self._server.get_player_move(self._dim)
            if y == False:
                self._server.wrong_coord(self._dim)
        return x-1, y-1

    def player_make_move(self):

        good_move = False
        while not good_move:
            move = self.player_get_move()
            good_move = self._board.set_point(move[0], move[1], self._actual_player)
            if not good_move:
                self._server.wrong_move()

        self._server.draw_board(self._board.get_board_state(), self._dim)

        if self._board.is_over():
            self._server.congratulate_winner(self._actual_player)
            is_end = True

        elif self._board.is_move_available():   # change player
            if self._actual_player == 'X':
                self._actual_player = 'O'
            else:
                self._actual_player = 'X'
            is_end = False

        else:
            self._server.announce_draw()
            is_end = True

        self._server.change_conn()

        return is_end
