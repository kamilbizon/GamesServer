from client.TicTacToeClient import TicTacToeClient
from client.MoreLessClient import MoreLessClient
from client.ConnectServerClient import ConnectServerClient
from Message import OnlineMessage
import socket


def main():
    connect_server_client = ConnectServerClient()
    type_game = connect_server_client.connect_server()
    print(type_game)

    if type_game == 'TIC':
        client = TicTacToeClient(connect_server_client.get_socket())
    elif type_game == "ML":
        client = MoreLessClient(connect_server_client.get_socket())
    else:
        exit()


if __name__ == '__main__':
    main()