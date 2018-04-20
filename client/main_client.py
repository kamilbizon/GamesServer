from client.tictactoeClient.TicTacToeClient import TicTacToeClient
from client.morelessClient.MoreLessClient import MoreLessClient
from client.connectClient.ConnectServerClient import ConnectServerClient


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