from server.TicTacToeGameOnline import TicTacToeGame
from server.MoreLessGame import MoreLessGame
from server.Server import Server
from Message import OnlineMessage


def ask_game(server):
    server.connect_player()
    player = server.get_player_list()
    message = OnlineMessage('AG')
    server.sent(message.encode(), player[0])
    message.decode(server.get(player[0]))

    while message.get_header() not in ['TIC', 'ML']:
        message.set_header('WG')
        server.sent(message.encode(), player[0])
        message.decode(server.get(player[0]))

    if message.get_header() == 'TIC':
        server.connect_player()
    return message.get_header()


def main():
    server = Server()
    type_game = ask_game(server)
    if type_game == 'TIC':
        game = TicTacToeGame(server)
    else:
        game = MoreLessGame()
    game.start_game()


if __name__ == '__main__':
    main()