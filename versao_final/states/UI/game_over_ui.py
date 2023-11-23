from __future__ import annotations
from states.UI.ui import UI
from buttons.text_button import TextButton
import pygame
import states.level_select_state as level_select_state



class GameOverUI(UI):
    def __init__(self, context):
        super().__init__(context)
        self.title= pygame.font.Font('assets/fonts/OldeEnglish.ttf',80).render('Jogo finalizado', True, 'black')
        self.buttons = [
               TextButton(pygame.font.Font(
                   'assets/fonts/Pixeltype.ttf',60)
                   .render('Sair',True,'black'),
                   'green',pygame.Rect(650,400,110,50),
                   lambda: context.change_state(level_select_state.LevelSelectState(context))),
               TextButton(pygame.font.Font(
                   'assets/fonts/Pixeltype.ttf',60)
                   .render('Jogar novamente',True,'black'),
                   'green',pygame.Rect(650,400,110,50),
                   lambda: context.change_state(level_select_state.LevelSelectState(context)))
        ]
        self.background = pygame.image.load('assets/backgrounds/basic_background.png')
    
    def draw_at(self, screen):
        screen.blit(self.background,(0,-100))
        screen.blit(self.title, (500,50))
        for button in self.buttons:
            button.draw_at(screen)