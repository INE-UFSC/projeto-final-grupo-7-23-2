from __future__ import annotations
import pygame

from entities.towers.tower import Tower
from entities.towers.archer_tower import ArcherTower
from entities.towers.catapult import Catapult
from factories.archer_tower_factory import ArcherTowerFactory
from factories.catapult_factory import CatapultFactory
from singletons.constants import Constants as C
import states.in_game_state as in_game_state

class Shop:
    def __init__(self, state: in_game_state.InGameState, money: float) -> None:
        self.__state = state
        self.__archer_factory = ArcherTowerFactory(25, 125, 1, 50, 100,  self.__state.get_projectiles(), self.__state.get_enemies())
        self.__catapult_factory = CatapultFactory(25, 125, 1, 100, 150,  self.__state.get_projectiles(), self.__state.get_enemies())
        self.__money = money

    def add_tower(self, type_tower:type[Tower], position: tuple[int,int]):
        c = C()
        tile_x = position[0] // c.get_tile_size() * c.get_tile_size() + c.get_tile_size() / 2
        tile_y = position[1] // c.get_tile_size() * c.get_tile_size() + c.get_tile_size() / 2
        new_tower_position = pygame.Vector2(tile_x, tile_y)
        if type_tower==ArcherTower:
            return self.__archer_factory.create_tower(new_tower_position)
        elif type_tower==Catapult:
            return self.__catapult_factory.create_tower(new_tower_position)

    def can_buy_tower(self, type_tower:type[Tower]) -> bool:
        if type_tower==ArcherTower:
            factory = self.__archer_factory
        elif type_tower==Catapult:
            factory = self.__catapult_factory
        return self.__money >= factory.get_tower_price()

    def upgrade(self, type_tower: type[Tower]):
        if type_tower==ArcherTower:
            factory = self.__archer_factory
        elif type_tower==Catapult:
            factory = self.__catapult_factory
        if self.__money >= factory.get_upgrade_price():
            self.__money -= factory.get_upgrade_price()
            factory.upgrade()

    def buy_tower(self, type_tower:type[Tower]):
        if type_tower==ArcherTower:
            factory = self.__archer_factory
        elif type_tower==Catapult:
            factory = self.__catapult_factory
        self.__money -= factory.get_tower_price()

    def add_money(self, amount: float) -> None:
        self.__money += amount

    def get_money(self):
        return self.__money

