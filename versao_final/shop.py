import pygame
from factories.tower_factory import TowerFactory
from singletons.constants import Constants as C
from entities.enemy import Enemy
from states.state import State

class Shop:
    def __init__(self, state: State, money: float) -> None:
        self.__state = state
        self.__tower_factory = TowerFactory(50, 75, 1.5, 50, self.__state.get_projectiles(), 100)
        self.__money = money
    
    def buy_tower(self, target: Enemy, position: tuple[int,int]):
        self.__money -= self.__tower_factory.get_tower_price()
        c = C()
        tile_x = position[0] // c.get_tile_size() * c.get_tile_size() + c.get_tile_size() / 2
        tile_y = position[1] // c.get_tile_size() * c.get_tile_size() + c.get_tile_size() / 2
        new_tower_position = pygame.Vector2(tile_x, tile_y)
        return self.__tower_factory.create_tower(target, new_tower_position)
    
    def can_buy_tower(self) -> bool:
        return self.__money >= self.__tower_factory.get_tower_price()
    def upgrade(self):
        if self.__money >= self.__tower_factory.get_upgrade_price():
            self.__money -= self.__tower_factory.get_upgrade_price()
            self.__tower_factory.upgrade()
    
    def add_money(self, amount: float) -> None:
        self.__money += amount