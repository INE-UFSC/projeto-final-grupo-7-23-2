from __future__ import annotations
import pygame
import sys

from drawable import Drawable

import states.state as state
import game

from levels.map import Map
from entities.enemy import Enemy
from entities.tower import Tower
from entities.bullet import Bullet
from entities.player_base import PlayerBase
import states.UI.menu_ui as menu_ui

class InGameState(state.State):
    def __init__(self, context: game.Game, level_number: int):
        state.State.__init__(self, context, menu_ui.MenuUI(context) )

        self.__map = Map(level_number)
        path = self.__map.get_path()
        self.player_base = PlayerBase(path.get_end() + pygame.Vector2(40, 0))
        self.enemy = Enemy(path)
        self.bullets: list[Bullet] = []
        self.towers = [
            Tower(pygame.Vector2(450, 300), 250, self.enemy, 50, self.bullets),
            Tower(pygame.Vector2(770, 300), 250, self.enemy, 50, self.bullets),
            Tower(pygame.Vector2(1245, 300), 250, self.enemy, 50, self.bullets),
            Tower(pygame.Vector2(980, 660), 250, self.enemy, 50, self.bullets)
        ]

        self.drawables: list[Drawable] = [path, self.player_base, self.enemy, *self.towers]

    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    print(pygame.mouse.get_pos())

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self, delta_time: float) -> None:
        self.enemy.update(delta_time)
        for tower in self.towers:
            tower.update(delta_time)

        for bullet in self.bullets:
            bullet.update(delta_time)
            if bullet.get_position().distance_to(self.enemy.get_position()) < 10:
                self.bullets.remove(bullet)
                self.enemy.take_damage(bullet.get_damage())
                # if not self.enemy.is_alive():
                #     print('inimigo morreu')
                #     pygame.quit()
                #     sys.exit()

        # if self.enemy.finished_path():
        #     print('inimigo chegou na base')
        #     pygame.quit()
        #     sys.exit()

    def render(self) -> None:
        screen = self.get_ctx().get_screen()

        self.__map.draw_at(screen)

        for drawable in self.drawables:
            drawable.draw_at(screen)

        for bullet in self.bullets:
            bullet.draw_at(screen)

