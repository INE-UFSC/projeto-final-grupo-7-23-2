from entities.enemies.enemy import Enemy
from path import Path
from singletons.constants import Constants as C

class Ogre(Enemy):
    def __init__(self, path: Path):
        image_paths = C().get_enemy_sprites('ogre', 6)
        super().__init__(path, 350.0, 50.0, image_paths)
    
    def take_damage(self, damage: int) -> None:
        return super().take_damage(damage - 15)
