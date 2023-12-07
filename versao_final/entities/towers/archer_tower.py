import pygame
from entities.towers.tower import Tower
from animation import Animation
from singletons.constants import Constants as C
from entities.enemies.enemy import Enemy
from entities.projectiles.arrow import Arrow
from entities.projectiles.projectile import Projectile


class ArcherTower(Tower):
    def __init__(self, position: pygame.Vector2, range: float, damage: float, shoot_rate: float, bullets_list: list[Projectile], enemies: list[Enemy], image_paths: list[str]):
        super().__init__(position, range, damage, shoot_rate, bullets_list, enemies, image_paths)

        archer_idle_images : list[pygame.Surface] = []
        for image_path in C().get_archer_sprites('idle',4):
            archer_idle_images.append(pygame.image.load(image_path))

        archer_atk_images : list[pygame.Surface] = []
        for image_path in C().get_archer_sprites('attack', 6):
            archer_atk_images.append(pygame.image.load(image_path))
        
        self.__idle_archer_animation = Animation(archer_idle_images, 10)
        self.__atk_archer_animation = Animation(archer_atk_images, 10)
    
    def draw_at(self, screen: pygame.Surface):

        image = self.get_animation().get_current_image()
        image_rect = image.get_rect(midbottom = self.get_position())

        archer_image = self.get_archer_animation().get_current_image()
        archer_rect = archer_image.get_rect(centerx = image_rect.centerx, centery= image_rect.centery - 20)
        screen.blit(image, image_rect)
        screen.blit(archer_image, archer_rect)
    
    def update(self, delta_time: float) -> None:
        self.get_state()()
        self.get_archer_animation().update()
    
    def create_projectile(self):
        return Arrow(self.get_position() - self.get_aim_vector(), self.get_target(), self.get_damage())
        
    def get_archer_animation(self):
        if self.get_state() == self.get_idle_state():
            return self.__idle_archer_animation
        return self.__atk_archer_animation
