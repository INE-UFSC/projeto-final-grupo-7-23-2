import pygame
from entities.tower import Tower

'''
Uma classe para criar torres. Criamos essa classe pois achamos a forma mais fácil e garantida de que, ao dar upgrade numa torre, todas as futuras torres viessem com atributos aprimorados.
Logo, o método upgrade() foi dado a essa classe, e não a torre. Ele muda os atributos da torre que determinam os atributos de torres criadas por ela.
Assim, ao invés de aprimorar os atributos de uma instância específica de torre, garantimos que todas as futras torres criadas por nossa Factory sejam melhores!
'''
#Obs: isto é uma classe que implementa a ideia mais básica de torre. A ideia é que classes filhas sejam feitas a partir dessa, cada uma criando uma classe-filha de torre diferente (Factory Method Design Pattern)
class Tower_Factory:
    def __init__(self, tower_dmg, tower_range, tower_price):
        self.tower_dmg = tower_dmg
        self.tower_range = tower_range
        self.tower_price = tower_price
    
    def create_tower(self, position: pygame.Vector2):
        return Tower(position, self.tower_range, self.tower_dmg, self.tower_price)
    
    def upgrade(self):
        self.tower_dmg *= 1.5
        self.tower_range *= 1.5
        self.tower_price *= 1.5