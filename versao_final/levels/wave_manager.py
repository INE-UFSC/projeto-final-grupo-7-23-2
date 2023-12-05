import json

from levels.wave import Wave
from entities.enemies.enemy import Enemy
from singletons.constants import Constants as C


class WaveManager:
    def __init__(self, map_number: int, enemies_ref: list[Enemy]):
        with open(C().get_map_waves_path(map_number)) as file:
            data = json.load(file)

        self.__waves: list[Wave] = []
        for wave in data['waves']:
            self.__waves.append()


    def update(self, delta_time: float) -> None:
        pass
