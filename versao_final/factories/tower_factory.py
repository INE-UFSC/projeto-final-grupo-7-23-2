import pygame

from entities.tower import Tower
from entities.enemies.enemy import Enemy
from entities.projectile import Projectile

'''
Uma classe para criar torres. Criamos essa classe pois achamos a forma mais fácil e garantida de que, ao dar upgrade numa torre, todas as futuras torres viessem com atributos aprimorados.
Logo, o método upgrade() foi dado a essa classe, e não a torre. Ele muda os atributos da torre que determinam os atributos de torres criadas por ela.
Assim, ao invés de aprimorar os atributos de uma instância específica de torre, garantimos que todas as futras torres criadas por nossa Factory sejam melhores!
'''
# Obs: isto é uma classe que implementa a ideia mais básica de torre.
# A ideia é que classes filhas sejam feitas a partir dessa, cada uma criando uma classe-filha
# de torre diferente (Factory Method Design Pattern)
class TowerFactory:
    def __init__(self, tower_dmg: float, tower_range: float, tower_shoot_rate: float, tower_price: float, projectiles_ref: list[Projectile], upgrade_price: float):
        self.__tower_dmg = tower_dmg
        self.__tower_range = tower_range
        self.__tower_price = tower_price
        self.__shoot_rate = tower_shoot_rate
        self.__projectiles_ref = projectiles_ref
        self.__upgrade_price = upgrade_price

    def create_tower(self,target: Enemy, position: pygame.Vector2):
        return Tower(position, self.__tower_range, target, self.__tower_dmg, self.__shoot_rate, self.__projectiles_ref)

    def upgrade(self):
        self.__tower_dmg *= 1.5
        self.__tower_range *= 1.5
        self.__shoot_rate *= 1.5

    def get_tower_price(self) -> float:
        return self.__tower_price

    def get_upgrade_price(self) -> float:
        return self.__upgrade_price
