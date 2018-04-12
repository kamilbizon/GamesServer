from Server.game_online import Game
from Server import Server

def main():
    server = Server()
    game = Game()
    game.start_game()


if __name__ == '__main__':
    main()