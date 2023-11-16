import pygame
from entity import Entity

class Damageable(Entity):
    def __init__(self, position: pygame.Vector2):
        super().__init__(position)
        self.hp = 0

    def take_damage(self, amount: float):
        self.hp -= self.amount