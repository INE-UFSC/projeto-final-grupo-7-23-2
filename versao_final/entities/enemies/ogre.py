import pygame
from entities.enemies.enemy import Enemy
from path import Path

class Ogre(Enemy):
    def __init__(self, path: Path):
        super().__init__(path)
        self.__speed = 70.0
        self.__health = 500
        self.__image = pygame.transform.flip (pygame.image.load('assets/entities/enemies/ogre/basic_ogre.png'), True, False)
    
    def take_damage(self, damage: int) -> None:
        return super().take_damage(damage - 15)