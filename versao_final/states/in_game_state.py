from __future__ import annotations
import pygame

from drawable import Drawable

import states.state as state
import game

from levels.map import Map
from factories.tower_factory import TowerFactory
from entities.enemy import Enemy
from entities.tower import Tower
from entities.projectile import Projectile
from entities.player_base import PlayerBase
from singletons.constants import Constants as C

import states.UI.menu_ui as menu_ui


class InGameState(state.State):
    def __init__(self, context: game.Game, level_number: int):
        # FIX: alterar menuUI para ingameUI quando for criado
        state.State.__init__(self, context, menu_ui.MenuUI(context) )

        self.__map = Map(level_number)
        path = self.__map.get_path()
        self.__player_base = PlayerBase(path.get_end() + pygame.Vector2(40, 0))
        self.__enemy = Enemy(path)

        self.__projectiles: list[Projectile] = []
        self.__tower_factory = TowerFactory(self.__enemy, 50, 75, 1.5, 50, self.__projectiles)
        self.__towers: list[Tower] = []

        self.__place_tower = False

    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.get_ctx().exit_game()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    c = C()
                    position = pygame.mouse.get_pos()
                    tile_x = position[0] // c.get_tile_size() * c.get_tile_size() + c.get_tile_size() / 2
                    tile_y = position[1] // c.get_tile_size() * c.get_tile_size() + c.get_tile_size() / 2
                    tower_position = pygame.Vector2(tile_x, tile_y)

                    self.__towers.append(self.__tower_factory.create_tower(tower_position))

                elif event.button == pygame.BUTTON_RIGHT:
                    self.__tower_factory.upgrade()

            elif event.type == pygame.QUIT:
                self.get_ctx().exit_game()

    def update(self, delta_time: float) -> None:
        self.__enemy.update(delta_time)
        for tower in self.__towers:
            tower.update(delta_time)

        for projectile in self.__projectiles:
            projectile.update(delta_time)
            if projectile.get_position().distance_to(self.__enemy.get_position()) < 10:
                self.__projectiles.remove(projectile)
                self.__enemy.take_damage(projectile.get_damage())
                # if not self.enemy.is_alive():
                #     print('inimigo morreu')
                #     pygame.quit()
                #     sys.exit()

        # if self.__place_tower:
        #     self.__place_tower = False
        #     new_tower = Tower(pygame.Vector2(pygame.mouse.get_pos()), 250, self.__enemy, 50, self.__projectiles)
        #     self.__towers.append(new_tower)
        #     self.__drawables.append(new_tower)

        # if self.enemy.finished_path():
        #     print('inimigo chegou na base')
        #     pygame.quit()
        #     sys.exit()

    def render(self) -> None:
        screen = self.get_ctx().get_screen()

        self.__map.draw_at(screen)

        for tower in self.__towers:
            tower.draw_at(screen)

        self.__enemy.draw_at(screen)
        self.__player_base.draw_at(screen)

        for projectile in self.__projectiles:
            projectile.draw_at(screen)

