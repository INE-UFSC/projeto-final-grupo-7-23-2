from __future__ import annotations
import states.state_interfaces as state_interfaces


class InitialState(state_interfaces.State):
    def __init__(self, context: state_interfaces.Context):
        state_interfaces.State.__init__(self, context)
