from client.MenuOutput import MenuOutput


class ConsoleMenuOutput(MenuOutput):

    def ask_game(self):
        print("What game you want to play: TicTacToe or MoreOrLess, write TIC or ML")

    def wrong_game_name(self):
        print("Wrong game name")

    def waiting_for_second_player(self):
        print("Wait for second player")

    def join_tic_tac_toe_game(self):
        print("You join TicTacToe game")

    def breaking_connection_server(self):
        print("Breaking communication with the server")

    def server_close_connection(self):
        print("Server closed connection")

    def cannot_connect_server(self):
        print("Cannot connect to server")

    def no_response(self):
        print("No response")