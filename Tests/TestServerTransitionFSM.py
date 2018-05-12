import unittest
from unittest.mock import Mock
from server.ServerTransitionFSM import ServerTransitionFSM, Event, State
from client.connectClient.ConnectServerClient import ConnectServerClient
from server.Server import Server


class TestServerTransitionFSM(unittest.TestCase):

    server = Server()


    def test_handle_event_call_connect_first_player_for_start_server_state_start_play_event(self):
        self.server.connect_first_player = Mock()

        fsm = ServerTransitionFSM(self.server)

        fsm.handle_event(Event.START_PLAY)
        self.assertTrue(fsm.state == State.CONNECT_FIRST_PLAYER)
        self.server.connect_first_player.assert_called()

    def test_handle_event_call_ask_game_for_connect_first_player_state_player_connected_event(self):
        self.server.ask_game = Mock()

        fsm = ServerTransitionFSM(self.server)
        fsm.state = State.CONNECT_FIRST_PLAYER

        fsm.handle_event(Event.PLAYER_CONNECTED)
        self.assertTrue(fsm.state == State.ASK_PLAYER_GAME)
        self.server.ask_game.assert_called()
