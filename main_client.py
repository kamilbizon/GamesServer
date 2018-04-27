from client.tictactoeClient.TicTacToeClient import TicTacToeClient
from client.morelessClient.MoreLessClient import MoreLessClient
from client.connectClient.ConnectServerClient import ConnectServerClient


def main():
    client = ConnectServerClient()
    type_game = client.connect_server()

    if type_game == 'TIC':
        client = TicTacToeClient(client.get_socket())
    elif type_game == "ML":
        client = MoreLessClient(client.get_socket())
    else:
        exit()


if __name__ == '__main__':
    main()