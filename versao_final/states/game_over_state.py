from __future__ import annotations
import states.state as state
import pygame
import game
import sys
from singletons.constants import Constants as C
from buttons.text_button import TextButton
import states.level_select_state as level_select_state

class GameOverState(state.State):
    def __init__(self, context: game.Game):
        state.State.__init__(self, context)
    
        width = C().get_screen_width()
        height = C().get_screen_height()

        self.title= pygame.font.Font('assets/fonts/OldeEnglish.ttf',80).render('Jogo finalizado', True, 'black')

        click_sound = pygame.mixer.Sound(C().get_sound('basic_click.wav'))

        self.buttons = [
               TextButton(pygame.font.Font(
                   C().get_font('Pixeltype.ttf'),60)
                   .render('Sair',True,'black'),
                   'red', width/2, height/3, width/11, height/14,
                   click_sound,
                   lambda: self.get_ctx().exit_game()),

               TextButton(pygame.font.Font(
                   C().get_font('Pixeltype.ttf'),60)
                   .render('Jogar novamente',True,'black'),
                   'green',width/2, 1.5*height/3, 3*width/11, height/14,
                   click_sound,
                   lambda: context.change_state(level_select_state.LevelSelectState(context)))
        ]

        self.background = pygame.image.load('assets/backgrounds/basic_background.png')

    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_buttons(pygame.mouse.get_pos())

    def draw_at(self, screen):
        screen.blit(self.background, self.background.get_rect(center = (C().get_screen_width()/2,C().get_screen_height()/2)))
        screen.blit(self.title, self.title.get_rect(center=(C().get_screen_width()/2,50)))
        for button in self.buttons:
            button.draw_at(screen)

    def update(self, delta_time: float) -> None:
        return
