from server.TicTacToeGameOnline import TicTacToeGame
from server.MoreLessOnline import MoreLessGame
from server.Server import Server
from Message import OnlineMessage


def ask_game(server):
    server.connect_player()
    player = server.get_player_list()
    message = OnlineMessage('AG')
    server.sent(message.encode(), player[0])
    message.decode(server.get(player[0]))
    type_game = message.get_header()

    if type_game not in ['TIC', 'ML']:
        pass

    if type_game == 'TIC':
        server.connect_player()
        players = server.get_player_list()
        message.set_header('JG') # join game
        server.sent(message.encode(), players[1])

    return type_game


def main():
    server = Server()
    type_game = ask_game(server)
    if type_game == 'TIC':
        game = TicTacToeGame(server)
    else:
        game = MoreLessGame(server)
    game.start_game()


if __name__ == '__main__':
    main()