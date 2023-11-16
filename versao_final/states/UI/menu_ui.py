from __future__ import annotations
from states.UI.ui import UI
from buttons.text_button import TextButton
import pygame
import states.level_select_state as level_select_state
class MenuUI(UI):
    def __init__(self, context):
        super().__init__(context)
        self.buttons = [
               TextButton(pygame.font.Font('assets/fonts/Pixeltype.ttf',14).render('Jogar',True,'black'),'green',pygame.Rect(200,700,50,20),lambda: context.change_state(level_select_state.LevelSelectState(context)))
        ]
    def render(self, screen):
        for button in self.buttons:
            button.draw(screen)