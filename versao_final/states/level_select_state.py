from states.state import State
from states.UI.level_select_ui import LevelSelectUI
import pygame
import sys

class LevelSelectState(State):
    def __init__(self, context):
        super().__init__(context, LevelSelectUI(context))
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_buttons(pygame.mouse.get_pos())
    def update(self, delta_time: float) -> None:
        return