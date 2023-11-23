from __future__ import annotations
import states.state as state
import pygame
import game

from states.UI.instructions_ui import InstructionsUI

class InstructionsState(state.State):
    def __init__(self, context: game.Game):
        super().__init__(context, InstructionsUI(context))
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.get_ctx().exit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_buttons(pygame.mouse.get_pos())
            elif event.type == pygame.QUIT:
                self.get_ctx().exit_game()
    def update(self, delta_time: float):
        return

