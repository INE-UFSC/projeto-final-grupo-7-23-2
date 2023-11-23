from __future__ import annotations
from states.UI.ui import UI
from buttons.text_button import TextButton
import pygame
import states.in_game_state as in_game_state
import states.menu_state as menu_state
from singletons.constants import Constants as C


class LevelSelectUI(UI):
    def __init__(self, context) -> None:
        super().__init__(context)
        self.buttons = [ 
            TextButton(
                pygame.font.Font('assets/fonts/Pixeltype.ttf', 42).render('Fase 1', True, 'black'),
                'green',
                pygame.Rect(300, 400, 95, 35),
                lambda: context.change_state(in_game_state.InGameState(context, 0))
            ),
            TextButton(
                pygame.font.Font('assets/fonts/Pixeltype.ttf', 42).render('Fase 2', True, 'black'),
                'green',
                pygame.Rect(600, 400, 95, 35),
                lambda: context.change_state(in_game_state.InGameState(context, 0))
            ),
            TextButton(
                pygame.font.Font('assets/fonts/Pixeltype.ttf', 42).render('Fase 3', True, 'black'),
                'green',
                pygame.Rect(900, 400, 95, 35),
                lambda: context.change_state(in_game_state.InGameState(context, 0))
            ),
            TextButton(
                pygame.font.Font('assets/fonts/Pixeltype.ttf', 42).render('Retornar', True, 'black'),
                'red',
                pygame.Rect(590, 650, 135, 35),
                lambda: context.change_state(menu_state.MenuState(context))
            )
        ]
        self.title = pygame.font.Font('assets/fonts/Pixeltype.ttf', 80).render('Escolha uma Fase', True, 'black')
        self.background = pygame.image.load('assets/backgrounds/basic_background.png')

    def draw_at(self, screen: pygame.Surface) -> None:
        screen.blit(self.background, self.background.get_rect(center = (C().get_width()/2,C().get_height()/2)))
        screen.blit(self.title, self.title.get_rect(center=(screen.get_rect().centerx, 100)))

        for button in self.buttons:
            button.draw_at(screen)

