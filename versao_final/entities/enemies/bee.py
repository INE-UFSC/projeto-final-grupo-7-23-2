import pygame
from entities.enemies.enemy import Enemy
from path import Path
import random

class Bee(Enemy):
    def __init__(self, path: Path):
        super().__init__(path)
        self.__speed = 170
        self.__health = 180
        self.__image = pygame.transform.flip (pygame.image.load('assets/entities/enemies/bee/basic_bee.png'), True, False)

    def take_damage(self, damage: int) -> None:
        chance = random.randint(1,4)
        if chance != 1:
            return super().take_damage(damage)