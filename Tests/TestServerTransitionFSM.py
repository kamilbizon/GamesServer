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

    def test_handle_event_call_start_more_less_game_for_ask_player_game_state_player_choose_more_less_event(self):
        self.server.start_more_less_game = Mock()

        fsm = ServerTransitionFSM(self.server)
        fsm.state = State.ASK_PLAYER_GAME

        fsm.handle_event(Event.PLAYER_CHOOSE_MORE_LESS)
        self.assertTrue(fsm.state == State.PLAY_MORE_LESS)
        self.server.start_more_less_game.assert_called()

    def test_handle_event_call_connect_second_player_for_ask_player_game_state_player_choose_tic_tac_toe_event(self):
        self.server.connect_second_player = Mock()

        fsm = ServerTransitionFSM(self.server)
        fsm.state = State.ASK_PLAYER_GAME

        fsm.handle_event(Event.PLAYER_CHOOSE_TIC_TAC_TOE)
        self.assertTrue(fsm.state == State.CONNECT_SECOND_PLAYER)
        self.server.connect_second_player.assert_called()

    def test_handle_event_call_start_tic_tac_toe_game_for_connect_second_player_state_player_connected_event(self):
        self.server.start_tic_tac_toe_game = Mock()

        fsm = ServerTransitionFSM(self.server)
        fsm.state = State.CONNECT_SECOND_PLAYER

        fsm.handle_event(Event.PLAYER_CONNECTED)
        self.assertTrue(fsm.state == State.PLAY_TIC_TAC_TOE)
        self.server.start_tic_tac_toe_game.assert_called()

    def test_handle_event_call_disconnect_players_for_play_more_less_state_game_finished_event(self):
        self.server.disconnect_players = Mock()

        fsm = ServerTransitionFSM(self.server)
        fsm.state = State.PLAY_MORE_LESS

        fsm.handle_event(Event.GAME_FINISHED)
        self.assertTrue(fsm.state == State.START_SERVER)
        self.server.disconnect_players.assert_called()

    def test_handle_event_call_disconnect_players_for_play_tic_tac_toe_state_game_finished_event(self):
        self.server.disconnect_players = Mock()

        fsm = ServerTransitionFSM(self.server)
        fsm.state = State.PLAY_TIC_TAC_TOE

        fsm.handle_event(Event.GAME_FINISHED)
        self.assertTrue(fsm.state == State.START_SERVER)
        self.server.disconnect_players.assert_called()
