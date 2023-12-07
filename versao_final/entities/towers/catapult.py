import pygame
from entities.towers.tower import Tower
from entities.enemies.enemy import Enemy
from entities.projectiles.boulder import Boulder
from entities.projectiles.projectile import Projectile
from animation import Animation


class Catapult(Tower):
    def __init__(self, position: pygame.Vector2, range: float, damage: float, shoot_rate: float, bullets_list: list[Projectile], enemies: list[Enemy], image_paths: list[str], catapult_paths: list[str]):
        super().__init__(position, range, damage, shoot_rate, bullets_list, enemies, image_paths)

        weapon_images : list[pygame.Surface] = []
        for image_path in catapult_paths:
            weapon_images.append(pygame.image.load(image_path))
        
        self.__weapon_animation = Animation(weapon_images, 10)
    
    def update(self, delta_time: float) -> None:
        self.get_state()()
        if self.get_state() == self.get_shooting_state():
            self.get_weapon_animation().update()
    
    def draw_at(self, screen: pygame.Surface):
        image = self.get_animation().get_current_image()
        image_rect = image.get_rect(midbottom = self.get_position())

        weapon_image = self.get_weapon_animation().get_current_image()
        weapon_rect = weapon_image.get_rect(centerx = image_rect.centerx, centery= image_rect.centery - 20)
        screen.blit(image, image_rect)
        screen.blit(weapon_image, weapon_rect)
    
    def get_weapon_animation(self):
        return self.__weapon_animation

    def create_projectile(self):
        return Boulder(self.get_position() - self.get_aim_vector(), self.get_target(), self.get_damage(), self.get_enemies(), 50)