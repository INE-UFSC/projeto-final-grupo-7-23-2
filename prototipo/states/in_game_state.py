from __future__ import annotations
import pygame
import sys

import states.state as state
import game

from path import Path
from entities.enemy import Enemy


class InGameState(state.State):
    def __init__(self, context: game.Game):
        state.State.__init__(self, context)

        self.path = Path([
            pygame.Vector2(100, 100),
            pygame.Vector2(200, 100),
            pygame.Vector2(200, 200),
            pygame.Vector2(100, 200),
            pygame.Vector2(100, 300),
            pygame.Vector2(543.2, 444),
        ])

        self.enemy = Enemy(pygame.Vector2(100, 100), self.path)

    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def update(self, delta_time: float) -> None:
        self.enemy.update(delta_time)
        if self.enemy.finished_path():
            pygame.quit()
            sys.exit()

    def render(self) -> None:
        screen = self.get_ctx().get_screen()
        self.path.draw_at(screen)
        self.enemy.draw_at(screen)
