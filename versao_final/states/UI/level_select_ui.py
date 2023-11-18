from __future__ import annotations
from states.UI.ui import UI
from buttons.text_button import TextButton
import pygame
import states.in_game_state as in_game_state
import states.menu_state as menu_state
class LevelSelectUI(UI):
    def __init__(self, context) -> None:
        super().__init__(context)
        self.buttons = [ 
            TextButton(pygame.font.Font('assets/fonts/Pixeltype.ttf',42).render(' Fase1',True,'black'),'green',pygame.Rect(600,400,75,35),lambda: context.change_state(in_game_state.InGameState(context))),
            TextButton(pygame.font.Font('assets/fonts/Pixeltype.ttf',42).render(' Retornar',True,'black'),'red',pygame.Rect(600,800,125,35),lambda: context.change_state(menu_state.MenuState(context)))
        ]
    def render(self, screen):
        screen.fill('white')
        for button in self.buttons:
            button.draw(screen)