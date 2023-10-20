from __future__ import annotations
import states.state as state
from game import Game


class InitialState(state.State):
    def __init__(self, context: Game):
        state.State.__init__(self, context)
