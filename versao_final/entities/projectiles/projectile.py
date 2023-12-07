import pygame

from entities.entity import Entity
from entities.enemies.enemy import Enemy


class Projectile(Entity):
    def __init__(self, position: pygame.Vector2, target: Enemy, damage: float):
        Entity.__init__(self, position)
        self.__velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.__speed = 250
        self.__target = target
        self.__damage = damage

    def update(self, delta_time: float) -> None:
        self.__velocity = (self.__target.get_position() - self.get_position()).normalize() * self.__speed * delta_time
        self.set_position(self.get_position() + self.__velocity)

    def get_damage(self) -> float:
        return self.__damage

    def get_target(self):
        return self.__target

    def get_velocity(self):
        return self.__velocity
