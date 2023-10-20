import pygame
import sys

import states.state_interfaces as state_interfaces

from path import Path
from entities.enemy import Enemy


class InGameState(state_interfaces.State):
    def __init__(self, context: state_interfaces.Context):
        state_interfaces.State.__init__(self, context)

        self.path = Path([
            pygame.Vector2(100, 100),
            pygame.Vector2(200, 100),
            pygame.Vector2(200, 200),
            pygame.Vector2(100, 200),
            pygame.Vector2(100, 300),
            pygame.Vector2(543.2, 444),
        ])

        self.enemy = Enemy(pygame.Vector2(100, 100), self.path)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        self.enemy.update()
        if self.enemy.finished_path():
            pygame.quit()
            sys.exit()
