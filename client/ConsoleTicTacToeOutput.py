from TicTacToeOutput import TicTacToeOutput

class ConsoleTicTacToeOutput(TicTacToeOutput):

    def first(self, player):
        print("You are {} player, you are first".format(player))

    def second(self, player):
        print("You are {} player, you are second".format(player))

    def welcome(self):
        print("Welcome in TicTacToe!")

    def ask_board_size(self, player):
        print("What board size do you want? (Not less than 3): ")

    def wrong_size(self, player):
        print("Wrong board size!")

    def draw_board(self, board, dim = 3):
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
        else:
            return True

    def player_move(self, player):
        print("Player", player, "move")

    def get_coord(self, coord, player):
        print("Coordinate {}: ".format(coord))

    def wrong_coord(self, dim, player):
        print("Wrong value! Coordinates have to be integer from 1 to {}".format(dim))

    def wrong_move(self, player):
        print("Wrong move!")

    def congratulate_winner(self, winner):
        print("Congratulate", winner, "player, you win!")

    def announce_draw(self):
        print("It's a draw!")
