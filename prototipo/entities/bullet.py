import pygame

from entities.entity import Entity
from entities.enemy import Enemy


class Bullet(Entity):
    def __init__(self, position: pygame.Vector2, target: Enemy):
        Entity.__init__(self, position)
        self.__velocity: pygame.Vector2
        self.__speed = 500
        self.__target = target

    def update(self, delta_time: float) -> None:
        self.__velocity = (self.__target.get_position() - self.get_position()).normalize() * self.__speed * delta_time
        self.set_position(self.get_position() + self.__velocity)

    def draw_at(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (100, 30, 100), self.get_position(), 3)
