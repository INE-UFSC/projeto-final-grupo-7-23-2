import pygame
import sys

from states.initial_state import InitialState
from states.in_game_state import InGameState

from entities.enemy import Enemy
from path import Path


class Game():
    def __init__(self):
        self.__state = InGameState(self)
        pygame.init()

        self.__screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
        self.__is_running = True

    def run(self):
        clock = pygame.time.Clock()

        while self.__is_running:
            delta_time = clock.tick() / 1000.0
            self.update(delta_time)
            self.render()
            clock.tick(60)

    def update(self, delta_time: float = 0.0):
        quit_event = pygame.event.get(pygame.QUIT)
        if len(quit_event) > 0:
            self.set_is_running(False)
            return

        self.get_state().update()

    def render(self):
        self.get_state().render()

    def set_is_running(self, is_running: bool) -> None:
        self.__is_running = is_running

    def get_screen(self) -> pygame.Surface:
        return self.__screen
