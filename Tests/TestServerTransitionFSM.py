import unittest
from unittest.mock import Mock
from server.ServerTransitionFSM import ServerTransitionFSM, Event, State
from client.connectClient.ConnectServerClient import ConnectServerClient
from server.Server import Server


class TestServerTransitionFSM(unittest.TestCase):

    def test_handle_event_call_connect_first_player_for_start_server_state_start_play_event(self):
        server = Server()
        server.connect_first_player = Mock()

        fsm = ServerTransitionFSM(server)

        fsm.handle_event(Event.START_PLAY)
        self.assertTrue(fsm.state == State.CONNECT_FIRST_PLAYER)
        server.connect_first_player.assert_called_once()
