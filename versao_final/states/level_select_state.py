from __future__ import annotations
from states.state import State

import pygame
import game

from buttons.text_button import TextButton
import states.in_game_state as in_game_state
import states.menu_state as menu_state
from singletons.constants import Constants as C

class LevelSelectState(State):
    def __init__(self, context: game.Game):
        super().__init__(context)

        click_sound = pygame.mixer.Sound(C().get_sound('basic_click.wav'))

        self.buttons = [ 
                TextButton(
                    pygame.font.Font(C().get_font('Pixeltype.ttf'), 42).render('Fase 1', True, 'black'),
                    'green',
                    C().get_screen_width()/4, C().get_screen_height()/3, 95, 35,
                    click_sound,
                    lambda: context.change_state(in_game_state.InGameState(context, 0))
                ),
                TextButton(
                    pygame.font.Font(C().get_font('Pixeltype.ttf'), 42).render('Fase 2', True, 'black'),
                    'green',
                    2 * C().get_screen_width() / 4, C().get_screen_height() / 3, 95, 35,
                    click_sound,
                    lambda: context.change_state(in_game_state.InGameState(context, 1))
                ),
                TextButton(
                    pygame.font.Font(C().get_font('Pixeltype.ttf'), 42).render('Fase 3', True, 'black'),
                    'green',
                    3 * C().get_screen_width() / 4, C().get_screen_height() / 3, 95, 35,
                    click_sound,
                    lambda: context.change_state(in_game_state.InGameState(context, 2))
                ),
                TextButton(
                    pygame.font.Font(C().get_font('Pixeltype.ttf'), 42).render('Retornar', True, 'black'),
                    'red',
                    C().get_screen_width() / 2, 2 * C().get_screen_height() / 3, 140, 35,
                    click_sound,
                    lambda: context.change_state(menu_state.MenuState(context))
                )
            ]
    
        self.title = pygame.font.Font(C().get_font('Pixeltype.ttf'), 80).render('Escolha uma Fase', True, 'black')
        self.background = pygame.image.load('assets/backgrounds/basic_background.png')

    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.get_ctx().exit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_buttons(pygame.mouse.get_pos())
            elif event.type == pygame.QUIT:
                self.get_ctx().exit_game()
    
    def draw_at(self, screen: pygame.Surface) -> None:
        screen.blit(
            self.background,
            self.background.get_rect(
                center=(C().get_screen_width() / 2, C().get_screen_height() / 2)
            )
        )
        screen.blit(
            self.title,
            self.title.get_rect(center=(C().get_screen_width() / 2, 50))
        )

        for button in self.buttons:
            button.draw_at(screen)

    def update(self, delta_time: float) -> None:
        return