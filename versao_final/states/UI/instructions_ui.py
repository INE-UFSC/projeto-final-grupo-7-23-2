from __future__ import annotations
import pygame
from states.UI.ui import UI
import game
from buttons.text_button import TextButton
from singletons.constants import Constants as C
import states.menu_state as menu_state

class InstructionsUI(UI):
    def __init__(self, context: game.Game) -> None:
        super().__init__(context)
        self.buttons = [
            TextButton(pygame.font.Font(C().get_font('Pixeltype.ttf'),42).render('Retornar',True,'black'),'red',C().get_width()/2,2*C().get_height()/3,140,35, lambda: context.change_state(menu_state.MenuState(context)))
        ]
        self.title= pygame.font.Font(C().get_font('Pixeltype.ttf'),80).render('Como Jogar', True, 'black')
        self.background = pygame.image.load('assets/backgrounds/basic_background.png')
    def draw_at(self, screen):
        screen.blit(self.background, self.background.get_rect(center = (C().get_width()/2,C().get_height()/2)))
        screen.blit(self.title, self.title.get_rect(center=(C().get_width()/2,50)))
        for button in self.buttons:
            button.draw_at(screen)