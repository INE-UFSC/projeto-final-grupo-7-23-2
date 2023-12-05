from entities.enemies.enemy import Enemy
from entities.enemies.bee import Bee
from entities.enemies.ogre import Ogre
from entities.enemies.wolf import Wolf


class Wave:
    def __init__(self, enemies_data: dict, enemies_ref: list[Enemy]):
        self.__enemies: list[Enemy] = []
        for 
