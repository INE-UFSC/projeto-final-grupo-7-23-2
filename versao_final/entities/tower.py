import pygame
from entity import Entity
from enemy import Enemy


class Tower(Entity):
    def __init__(self, position: pygame.Vector2, range: float, damage: int, price: float):
        Entity.__init__(self, position)
        self.__state = self.watching_target
        self.__range = range
        self.target: Enemy
        self.damage = damage
        self.price = price

    def watching_target(self):
        if self.get_position().distance_to(self.__target.get_position()) < self.__range:
            self.__state = self.shooting_target


    def shooting_target(self):
        pass
