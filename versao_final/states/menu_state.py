from __future__ import annotations
import states.state as state
import pygame
import game

import states.level_select_state as level_select_state
import states.instructions_state as instructions_state

from singletons.constants import Constants as C

from buttons.text_button import TextButton

class MenuState(state.State):
    def __init__(self, context: game.Game):
        state.State.__init__(self, context)

        click_sound = pygame.mixer.Sound(C().get_sound('basic_click.wav'))
        #self.__music = pygame.mixer.Sound(C().get_sound(''))

        self.buttons = [
            TextButton(
                pygame.font.Font(C().get_font('Pixeltype.ttf'), 60).render('Jogar', True, 'black'),
                'green',
                C().get_screen_width() / 2, C().get_screen_height() / 4,
                125, 55,
                click_sound,
                lambda: self.get_ctx().change_state(level_select_state.LevelSelectState(context))
            ),
            TextButton(
                pygame.font.Font(C().get_font('Pixeltype.ttf'), 60).render('Como Jogar', True, 'black'),
                'cyan',
                C().get_screen_width() / 2, 1.75 * C().get_screen_height() / 4,
                230, 55,
                click_sound,
                lambda: self.get_ctx().change_state(instructions_state.InstructionsState(context))
            ),
            TextButton(
                pygame.font.Font(C().get_font('Pixeltype.ttf'), 60).render('Sair', True, 'black'),
                'red',
                C().get_screen_width() / 2, 2.5 * C().get_screen_height() / 4,
                105, 55,
                click_sound,
                lambda: self.get_ctx().exit_game()
            )
        ]
        self.title= pygame.font.Font('assets/fonts/OldeEnglish.ttf', 80).render('Guardiões das Torres', True, 'black')
        self.background = pygame.image.load('assets/backgrounds/basic_background.png')

    def handle_input(self) -> None:
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
        screen.blit(self.title, self.title.get_rect(center=(C().get_screen_width()/2,50)))

        for button in self.buttons:
            button.draw_at(screen)
    
    def update(self, delta_time: float) -> None:
        return
