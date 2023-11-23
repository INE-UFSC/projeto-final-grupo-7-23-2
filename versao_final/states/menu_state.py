from __future__ import annotations
import states.state as state
import pygame
import game
from states.UI.menu_ui import MenuUI

class MenuState(state.State):
    def __init__(self, context: game.Game):
        state.State.__init__(self, context, MenuUI(context))

    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.get_ctx().exit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_buttons(pygame.mouse.get_pos())
            elif event.type == pygame.QUIT:
                self.get_ctx().exit_game()
    def update(self, delta_time: float) -> None:
        return
