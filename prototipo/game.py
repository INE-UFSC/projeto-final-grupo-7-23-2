import pygame
import sys

from entities.enemy import Enemy
from path import Path


class Game:
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)

        self.__is_running = True

        self.path = Path([
            pygame.Vector2(100, 100),
            pygame.Vector2(200, 100),
            pygame.Vector2(200, 200),
            pygame.Vector2(100, 200),
            pygame.Vector2(100, 300),
            pygame.Vector2(543.2, 444),
        ])

        self.enemy = Enemy(pygame.Vector2(100, 100), self.path)

    def run(self):
        clock = pygame.time.Clock()

        while self.__is_running:
            delta_time = clock.tick() / 1000.0
            self.update(delta_time)
            self.render()
            clock.tick(60)

    def update(self, delta_time: float = 0.0):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        self.enemy.update()
        if self.enemy.finished_path():
            pygame.quit()
            sys.exit()

    def render(self):
        self.__screen.fill((0, 0, 0))
        self.enemy.draw_at(self.__screen)
        self.path.draw_to(self.__screen)
        pygame.display.flip()

    def set_is_running(self, is_running: bool) -> None:
        self.__is_running = is_running

    def get_screen(self) -> pygame.Surface:
        return self.__screen
