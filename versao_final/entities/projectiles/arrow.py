import pygame
from entities.projectiles.projectile import Projectile
from entities.enemies.enemy import Enemy

class Arrow(Projectile):
    def __init__(self, position: pygame.Vector2, target: Enemy, damage: float, speed: int):
        Projectile.__init__(self, position, target, damage)

        self.__image = pygame.image.load('assets/entities/towers/arrow.png')
        self.__speed = speed
        self.__angle = 0

    def draw_at(self, screen):
        new_angle = self.get_velocity().angle_to(pygame.Vector2(1,0))
        rotate_angle = new_angle - self.__angle
        self.__image = pygame.transform.rotate(self.__image, rotate_angle)
        self.__angle = new_angle
        screen.blit(self.__image, self.get_position())
