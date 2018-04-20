from client.MenuInput import MenuInput


class ConsoleMenuInput(MenuInput):

    def get_game_name(self):
        answer = input()
        return answer