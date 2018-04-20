from server.TicTacToeGameOnline import TicTacToeGame
from server.MoreLessOnline import MoreLessGame
from server.Server import Server
from Message import OnlineMessage


def ask_game(server):
    server.connect_player()
    players = server.get_player_list()

    message = OnlineMessage()
    type_game = None
    while type_game not in ['TIC', 'ML']:
        message = OnlineMessage('AG')   # ask game
        server.send(message.encode(), players[0])
        message.decode(server.get(players[0]))
        type_game = message.get_header()

        if type_game not in ['TIC', 'ML']:
            message.set_header('WG') # join game
            server.send(message.encode(), players[0])

    message.set_header('CG')    # correct game
    message.set_body(type_game)
    server.send(message.encode(), players[0])

    if type_game == 'TIC':
        server.connect_player()
        message.set_header('JG') # join game
        players = server.get_player_list()
        server.send(message.encode(), players[1])

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