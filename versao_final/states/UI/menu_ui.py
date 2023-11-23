from __future__ import annotations
from states.UI.ui import UI
from buttons.text_button import TextButton
import pygame
import states.level_select_state as level_select_state
import states.instructions_state as instructions_state
from singletons.constants import Constants as C

class MenuUI(UI):
    def __init__(self, context):
        super().__init__(context)
        self.buttons = [
               TextButton(pygame.font.Font('assets/fonts/Pixeltype.ttf',60).render('Jogar',True,'black'),'green',C().get_width()/2,C().get_height()/4,125,55, lambda: self.get_ctx().change_state(level_select_state.LevelSelectState(context))),
               TextButton(pygame.font.Font('assets/fonts/Pixeltype.ttf',60).render('Como Jogar',True,'black'),'cyan',C().get_width()/2,1.75*C().get_height()/4,230,55, lambda: self.get_ctx().change_state(instructions_state.InstructionsState(context))),
               TextButton(pygame.font.Font('assets/fonts/Pixeltype.ttf',60).render('Sair',True,'black'),'red',C().get_width()/2,2.5*C().get_height()/4,105,55, lambda: self.get_ctx().exit_game() )
        ]
        self.title= pygame.font.Font('assets/fonts/OldeEnglish.ttf',80).render('Guardiões das Torres', True, 'black')
        self.background = pygame.image.load('assets/backgrounds/basic_background.png')
    def render(self, screen):
        screen.blit(self.background, self.background.get_rect(center = (C().get_width()/2,C().get_height()/2)))
        screen.blit(self.title, self.title.get_rect(center=(screen.get_rect().centerx,100)))
        for button in self.buttons:
            button.draw(screen)