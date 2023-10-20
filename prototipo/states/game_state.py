import states.state_interfaces as state_interfaces

from game import Game


class GameState(state_interfaces.State):
    def __init__(self, context: Game):
        state_interfaces.State.__init__(self, context)

    def get_ctx(self) -> Game:
