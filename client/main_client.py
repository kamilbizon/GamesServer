from client.TicTacToeClient import TicTacToeClient
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
        while answer not in ['T', 'L']:
            print("What game you want to play: TicTacToe or MoreOrLess, write T or L")
            answer = input()

        message = OnlineMessage('TIC')
        sock.send(message.encode())

    return sock


def main():
    socket = connect_server()
    client = TicTacToeClient(socket)

if __name__ == '__main__':
    main()