import pygame
from entities.projectiles.projectile import Projectile
from entities.enemies.enemy import Enemy

class Boulder(Projectile):
    def __init__(self, position: pygame.Vector2, target: Enemy, damage: float, enemies: list[Enemy], range: float):
        super().__init__(position, target, damage)
        self.__enemies = enemies
        self.__range = range
        self.__image = pygame.image.load('assets/entities/towers/catapult/boulder.png')
        self.__speed = 250
    
    def hit(self):
        for enemy in self.__enemies:
            if self.enemy_in_range(enemy):
                enemy.take_damage(self.get_damage())
    
    def draw_at(self, screen: pygame.Surface):
        screen.blit(self.__image, self.get_position())
    
    def enemy_in_range(self, enemy: Enemy):
        return self.get_position().distance_to(enemy.get_position()) < self.__range

    