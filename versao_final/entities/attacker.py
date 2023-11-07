import pygame
from entity import Entity
from damageable import Damageable

class Attacker(Entity):
    def __init__(self, position: pygame.Vector2):
        super().__init__(position)
        self.damage = 0
    
    def attack (self, target: Damageable):
        target.take_damage(self.damage)