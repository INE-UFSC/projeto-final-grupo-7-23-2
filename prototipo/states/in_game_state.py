from __future__ import annotations
import pygame
import sys

from drawable import Drawable

import states.state as state
import game

from path import Path
from entities.enemy import Enemy
from entities.tower import Tower


class InGameState(state.State):
    def __init__(self, context: game.Game):
        state.State.__init__(self, context)

        self.path = Path([
            pygame.Vector2(100, 540),
            pygame.Vector2(660, 540),
            pygame.Vector2(660, 100),
            pygame.Vector2(1300, 100),
            pygame.Vector2(1300, 540),
            pygame.Vector2(1750, 540),
        ])

        self.enemy = Enemy(self.path)
        self.towers = [
            Tower(pygame.Vector2(400, 300), 250, self.enemy),
            Tower(pygame.Vector2(770, 300), 250, self.enemy),
            Tower(pygame.Vector2(1245, 300), 250, self.enemy),
            Tower(pygame.Vector2(980, 660), 250, self.enemy)
        ]

        self.drawables: list[Drawable] = [self.path, self.enemy, *self.towers]

    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    print(pygame.mouse.get_pos())

    def update(self, delta_time: float) -> None:
        self.enemy.update(delta_time)
        for tower in self.towers:
            tower.update(delta_time)
        # if self.enemy.finished_path():
        #     pygame.quit()
        #     sys.exit()

    def render(self) -> None:
        screen = self.get_ctx().get_screen()
        for drawable in self.drawables:
            drawable.draw_at(screen)
