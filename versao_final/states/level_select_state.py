from __future__ import annotations
from states.state import State
from states.UI.level_select_ui import LevelSelectUI
import pygame
import game

class LevelSelectState(State):
    def __init__(self, context: game.Game):
        super().__init__(context, LevelSelectUI(context))
    
    def handle_input(self):
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