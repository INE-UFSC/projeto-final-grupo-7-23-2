from math import log
from entities.enemies.enemy import Enemy
from path import Path
import random
from singletons.constants import Constants as C

class Bee(Enemy):
    def __init__(self, path: Path):
        image_paths = C().get_enemy_sprites('bee', 6)
        super().__init__(path, 180.0, 100, image_paths)

    def take_damage(self, damage: int) -> None:
        chance = random.randint(1,4)
        if chance != 1:
            return super().take_damage(damage)
