from tictactoeInputOutputInterface.TicTacToeOutput import TicTacToeOutput


class ConsoleTicTacToeOutput(TicTacToeOutput):

    def first(self, player):
        print("You are {} player, you are first".format(player))

    def second(self, player):
        print("You are {} player, you are second".format(player))

    def welcome(self):
        print("Welcome in TicTacToe!")

    def ask_board_size(self, player=0):
        print("What board size do you want? (Not less than 3): ")

    def wrong_size(self, player=0):
        print("Wrong board size!")

    def draw_board(self, board, dim=3):
        for i in range(dim):
            if i != 0:
                for k in range(dim - 1):
                    print('--+', end='')
                print('--')
            for j in range(dim):
                if j < dim - 1:
                    print(''.join(board[i][j]), '|', end='')
                else:
                    print(''.join(board[i][j]))
        print()

    def player_move(self, player):
        print("Player", player, "move")

    def ask_coord(self, coord, player=0):
        print("Coordinate {}: ".format(coord))

    def wrong_coord(self, dim, player=0):
        print("Wrong value! Coordinates have to be integer from 1 to {}".format(dim))

    def wrong_move(self, player=0):
        print("Wrong move!")

    def congratulate_winner(self, winner):
        print(winner, "player win!")

    def announce_draw(self):
        print("It's a draw!")
