from __future__ import annotations
import states.state as state
import pygame
import game
import sys
from states.UI.game_over_ui import GameOverUI

class GameOverState(state.State):
    def __init__(self, context: game.Game):
        state.State.__init__(self, context, GameOverUI(context))

    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_buttons(pygame.mouse.get_pos())
    def update(self, delta_time: float) -> None:
        return
