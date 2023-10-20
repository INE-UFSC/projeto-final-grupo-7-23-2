from __future__ import annotations
import pygame
import sys

import states.state as state
import states.menu_state as menu_state
import game


class GameOverState(state.State):
    def __init__(self, context: game.Game):
        state.State.__init__(self, context)

    def handle_input(self) -> None:
        ...

    def update(self, delta_time: float) -> None:
        ...

    def render(self) -> None:
        ...
