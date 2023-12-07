from __future__ import annotations
import pygame

from entities.animated_entity import AnimatedEntity
from entities.enemies.enemy import Enemy
from entities.projectiles.projectile import Projectile
from singletons.constants import Constants as C


class Tower(AnimatedEntity):
    def __init__(self, position: pygame.Vector2, range: float, damage: float, shoot_rate: float, bullets_list: list[Projectile], enemies: list[Enemy], image_paths: list[str]):

        images: list[pygame.Surface] = []
        for image_path in image_paths:
            images.append(pygame.image.load(image_path))

        AnimatedEntity.__init__(self, position, images, 10)
        self.__state = self.__idle
        self.__range = range
        self.__shoot_rate = shoot_rate
        self.__damage = damage
        self.__bullets_list = bullets_list
        self.__enemies = enemies
        self.__target : Enemy = None
        self.__angle: float
        self.__aim_vector = pygame.Vector2(0, 0)
        self.__last_shoot = 0.0

        self.build_sound = pygame.mixer.Sound(C().get_sound('build_tower.wav'))
        self.build_sound.play()

    def __idle(self) -> None:
        for enemy in self.__enemies:
            if self.enemy_in_range(enemy):
                self.__target = enemy
                self.__state = self.__shooting_target
                return

    def __shooting_target(self) -> None:
        if not self.enemy_in_range(self.__target) or not self.__target.is_alive():
            self.__target = None
            self.__state = self.__idle
            return

        vector = self.get_position() - self.__target.get_position()
        vector.scale_to_length(50)
        self.__aim_vector = vector
        current_time = pygame.time.get_ticks()
        if current_time - self.__last_shoot > (1 / self.__shoot_rate) * 1000:
            self.__bullets_list.append(self.create_projectile())
            self.__last_shoot = current_time

    def enemy_in_range(self, enemy: Enemy) -> bool:
        return self.get_position().distance_to(enemy.get_position()) < self.__range
    
    def draw_at(self, screen: pygame.Surface):

        image = self.get_animation().get_current_image()
        image_rect = image.get_rect(midbottom = self.get_position())

        archer_image = self.get_archer_animation().get_current_image()
        archer_rect = archer_image.get_rect(centerx = image_rect.centerx, centery= image_rect.centery - 20)
        screen.blit(image, image_rect)
        screen.blit(archer_image, archer_rect)
    
    def update(self, delta_time: float) -> None:
        self.__state()
        self.get_animation().update()
    
    def get_enemies(self):
        return self.__enemies
    
    def create_projectile(self):
        return Projectile(self.get_position() - self.__aim_vector, self.__target, self.__damage)
    
    def get_state(self):
        return self.__state
    
    def get_idle_state(self):
        return self.__idle
    
    def get_shooting_state(self):
        return self.__shooting_target
    
    def get_aim_vector(self):
        return self.__aim_vector
    
    def get_damage(self):
        return self.__damage
    
    def get_target(self):
        return self.__target