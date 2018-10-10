[![Build Status](https://travis-ci.org/kamilbizon/GamesServer.svg?branch=master)](https://travis-ci.org/kamilbizon/GamesServer) [![Coverage Status](https://coveralls.io/repos/github/kamilbizon/GamesServer/badge.svg?branch=master)](https://coveralls.io/github/kamilbizon/GamesServer?branch=master)
# Games Server
This program is our implementation of simple client-server application with games within console terminal by TCP connection using the python language. You can choose singleplayer More or Less or multiplayer Tic Tac Toe.
## Installation
To be able to use this program simply download the contents of [this directory](). To work properly this program
requires that you have the [python interpreter](https://www.python.org/downloads/) installed too.
Next put all the files in a directory you would like to use it in.
## Usage
Assuming you have python installed, open the terminal
 on your computer no specific shell required. Next type
 `python3` on linux systems (`python` on windows) and then `main_server.py`, next connect client `main_client.py` to run the program. Client choose the game. If it is More or Less game starts. If first player choose Tic Tac Toe run again `main_client.py` to connect second player. After finished game server waits again for first client.
