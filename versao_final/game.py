from __future__ import annotations
import pygame

import states.state as state
from states.menu_state import MenuState
from states.game_over_state import GameOverState

class Game():
    def __init__(self):
        pygame.init()
        self.__state = MenuState(self)
        self.__state = GameOverState(self)

        self.__screen = pygame.display.set_mode((1280, 720))
        self.__is_running = True

    def run(self):
        clock = pygame.time.Clock()

        while self.__is_running:
            delta_time = clock.tick(60) / 1000.0
            self.handle_input()
            self.update(delta_time)
            self.render()
        pygame.quit()

    def handle_input(self):
        self.__state.handle_input()

    def update(self, delta_time: float = 0.0):
        self.__state.update(delta_time)

    def render(self):
        self.__screen.fill((0, 0, 0))
        self.__state.render()
        pygame.display.flip()

    def change_state(self, new_state: state.State) -> None:
        self.__state = new_state

    def set_is_running(self, is_running: bool) -> None:
        self.__is_running = is_running

    def get_screen(self) -> pygame.Surface:
        return self.__screen

