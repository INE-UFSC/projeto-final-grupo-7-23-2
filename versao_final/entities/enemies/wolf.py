from entities.enemies.enemy import Enemy
from path import Path
from singletons.constants import Constants as C

class Wolf(Enemy):
    def __init__(self, path: Path):
        image_paths = C().get_enemy_sprites('wolf', 6)
        super().__init__(path, 250.0, 170.0, image_paths)
