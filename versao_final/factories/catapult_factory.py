import pygame
from factories.tower_factory import TowerFactory
from entities.towers.catapult import Catapult
from entities.enemies.enemy import Enemy
from entities.projectiles.projectile import Projectile
from singletons.constants import Constants as C

class CatapultFactory(TowerFactory):
    def __init__(self, tower_dmg: float, tower_range: float, tower_shoot_rate: float, tower_price: float, upgrade_price: float, projectiles_ref: list[Projectile], enemies_ref: list[Enemy]):
        super().__init__(tower_dmg, tower_range, tower_shoot_rate, tower_price, upgrade_price, projectiles_ref, enemies_ref)
        self.__images_paths= C().get_tower_sprites('catapult', 0, 4)
        self.__catapult_paths = {0:C().get_weapon_sprites(0, 6),
                               1:C().get_weapon_sprites(0, 6),
                               2:C().get_weapon_sprites(2, 8)}
    
    def create_tower(self, position: pygame.Vector2):
        return    Catapult(position, self.get_tower_range(), self.get_tower_dmg(), self.get_tower_shoot_rate(), self.get_projectile_ref(), self.get_enemies_ref(), self.__images_paths, self.__catapult_paths[self.get_upgrade_amount()])