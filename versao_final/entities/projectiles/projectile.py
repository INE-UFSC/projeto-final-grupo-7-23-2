from __future__ import annotations
import pygame

from entities.entity import Entity
from entities.enemies.enemy import Enemy


class Projectile(Entity):
    def __init__(self, position: pygame.Vector2, target: Enemy, damage: float):
        Entity.__init__(self, position)
        self.__velocity: pygame.Vector2
        self.__speed = 250
        self.__target = target
        self.__damage = damage
        self.__velocity = pygame.Vector2(1,0)

    def update(self, delta_time: float) -> None:
        self.__velocity = (self.get_target().get_position() - self.get_position()).normalize() * self.__speed * delta_time
        self.set_position(self.get_position() + self.get_velocity())
    
    def hit(self):
        self.get_target().take_damage(self.get_damage())

    def get_damage(self) -> float:
        return self.__damage
    
    def get_target(self):
        return self.__target
    
    def get_velocity(self):
        return self.__velocity
    
    def get_tower(self):
        return self.__tower
