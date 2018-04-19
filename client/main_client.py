from client.TicTacToeClient import TicTacToeClient
from client.MoreLessClient import MoreLessClient
from Message import OnlineMessage
import socket


def connect_server():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(('127.0.0.1', 5005))
    except ConnectionRefusedError:
        print("Nie można połączyć się z serverem")
        exit()

    sock.settimeout(None)

    message = OnlineMessage()
    data = sock.recv(512)
    message.decode(data)

    if message.get_header() == 'AG': # ask game

        answer = None
        while answer not in ['TIC', 'ML']:
            print("What game you want to play: TicTacToe or MoreOrLess, write TIC or ML")
            answer = input()

        if answer == 'TIC':
            message = OnlineMessage('TIC')
            sock.send(message.encode())
        else:
            message = OnlineMessage('ML')
            sock.send(message.encode())
    else:
        answer = 'TIC'

    return sock, answer


def main():
    sock, answer = connect_server()
    if answer == 'TIC':
        client = TicTacToeClient(sock)
    elif answer == "ML":
        client = MoreLessClient(sock)
    else:
        exit()


if __name__ == '__main__':
    main()