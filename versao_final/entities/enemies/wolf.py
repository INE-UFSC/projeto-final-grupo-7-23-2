import pygame
from entities.enemies.enemy import Enemy
from path import Path

class Wolf(Enemy):
    def __init__(self, path: Path):
        super().__init__(path, 250.0, 100.0, pygame.transform.flip(pygame.image.load('assets/entities/enemies/wolf/basic.png'), True, False)  )