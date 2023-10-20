from __future__ import annotations
import pygame
import sys

import states.state as state
import states.in_game_state as in_game_state
import game


class MenuState(state.State):
    def __init__(self, context: game.Game):
        state.State.__init__(self, context)

    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_SPACE:
                    self.get_ctx().change_state(in_game_state.InGameState(self.get_ctx()))

    def update(self, delta_time: float) -> None:
        return

    def render(self) -> None:
        screen = self.get_ctx().get_screen()
        pygame.draw.circle(screen, (255, 0, 0), (100, 100), 10)
