from server.TicTacToeBoard import TicTacToeBoard
from server.TicTacToeTCP import TicTacToeTCP



class TicTacToeGame:
    players = ['O', 'X']

    def __init__(self, server):
        self._TCP = TicTacToeTCP(server)

        # no need for larger board atm
        # self._TCP.ask_board_size()
        #
        # dim = False
        # while not dim:
        #     dim = self._TCP.get_board_size()
        #     if not dim:
        #         self._TCP.wrong_size()

        self._dim = 3
        self._board = TicTacToeBoard(self._dim)


        self._actual_player = 'O'
        second_player = 'X'

        self._TCP.first_second(self._actual_player, second_player)

    def start_game(self):
        self._TCP.welcome()
        self._TCP.draw_board(self._board.get_board_state(), self._dim)

        is_end = False
        while not is_end:
            is_end = self.player_make_move()

    def player_get_move(self):
        self._TCP.player_move(self._actual_player)
        self._TCP.get_coord('x', self._actual_player)

        x = False
        while not x:
            x = self._TCP.get_player_move(self._dim, self._actual_player)
            if x == False:
                self._TCP.wrong_coord(self._dim, self._actual_player)

        self._TCP.get_coord('y', self._actual_player)
        y = False
        while not y:
            y = self._TCP.get_player_move(self._dim, self._actual_player)
            if y == False:
                self._TCP.wrong_coord(self._dim, self._actual_player)
        return x-1, y-1


    def player_make_move(self):
        good_move = False
        while not good_move:
            move = self.player_get_move()
            good_move = self._board.set_point(move[0], move[1], self._actual_player)
            if not good_move:
                self._TCP.wrong_move(self._actual_player)

        self._TCP.draw_board(self._board.get_board_state(), self._dim)

        if self._board.is_over():
            self._TCP.congratulate_winner(self._actual_player)
            is_end = True

        elif self._board.is_move_available():   # change player
            if self._actual_player == 'X':
                self._actual_player = 'O'
            else:
                self._actual_player = 'X'
            is_end = False

        else:
            self._TCP.announce_draw()
            is_end = True

        return is_end
