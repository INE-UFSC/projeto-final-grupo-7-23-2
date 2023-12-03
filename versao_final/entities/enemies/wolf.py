import pygame
from entities.enemies.enemy import Enemy
from path import Path

class Wolf(Enemy):
    def __init__(self, path: Path):
        super().__init__(path)
        self.__speed = 200.0
        self.__health = 250
        self.__image = pygame.transform.flip (pygame.image.load('assets/entities/enemies/wolf/basic.png'), True, False)