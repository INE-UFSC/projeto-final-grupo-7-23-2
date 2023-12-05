from entities.enemies.enemy import Enemy
from path import Path
from singletons.constants import Constants as C

class Wolf(Enemy):
    def __init__(self, path: Path):
        image_paths = C().get_enemy_sprites('wolf', 6)
        super().__init__(path, 50.0, 120.0, image_paths)
