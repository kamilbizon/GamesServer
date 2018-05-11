from server.Transition import Transition
import enum


class Event(enum.Enum):
    START_PLAY = 1
    PLAYER_CONNECTED = 2
    PLAYER_CHOOSE_MORE_LESS = 3
    PLAYER_CHOOSE_TIC_TAC_TOE = 4
    GAME_FINISHED = 5


class State(enum.Enum):
    START_SERVER = 1
    CONNECT_FIRST_PLAYER = 2
    ASK_PLAYER_GAME = 3
    PLAY_MORE_LESS = 4
    CONNECT_SECOND_PLAYER = 5
    PLAY_TIC_TAC_TOE = 6


class ServerTransitionFSM:

    def __init__(self, server):
        self.state = State.START_SERVER
        self.server = server
        self.transitions = [
            Transition(State.START_SERVER, Event.START_PLAY, State.CONNECT_FIRST_PLAYER, self.server.connect_first_player),
            Transition(State.CONNECT_FIRST_PLAYER, Event.PLAYER_CONNECTED, State.ASK_PLAYER_GAME, self.server.ask_game),
            Transition(State.ASK_PLAYER_GAME, Event.PLAYER_CHOOSE_MORE_LESS, State.PLAY_MORE_LESS, self.server.start_more_less_game),
            Transition(State.ASK_PLAYER_GAME, Event.PLAYER_CHOOSE_TIC_TAC_TOE, State.CONNECT_SECOND_PLAYER, self.server.connect_second_player),
            Transition(State.CONNECT_SECOND_PLAYER, Event.PLAYER_CONNECTED, State.PLAY_TIC_TAC_TOE, self.server.start_tic_tac_toe_game),
            Transition(State.PLAY_MORE_LESS, Event.GAME_FINISHED, State.START_SERVER, self.server.disconnect_players),
            Transition(State.PLAY_TIC_TAC_TOE, Event.GAME_FINISHED, State.START_SERVER, self.server.disconnect_players)
        ]

    def handle_event(self, event):
        for transition in self.transitions:
            if transition.event == event and transition.given_state == self.state:
                self.state = transition.next_state
                transition.action()
