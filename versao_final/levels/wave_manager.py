import json

from levels.wave import Wave
from entities.enemies.enemy import Enemy
from path import Path
from singletons.constants import Constants as C


class WaveManager:
    def __init__(self, map_number: int, enemies_ref: list[Enemy], path: Path):
        with open(C().get_map_waves_path(map_number), 'r') as file:
            data = json.load(file)

        self.__waves: list[Wave] = []
        for wave in data['waves']:
            self.__waves.append(Wave(wave['enemies'], enemies_ref, path, wave['delay']))

        self.__current_wave_index = 0
        self.__current_wave = self.__waves[self.__current_wave_index]

        self.__finished = False

    def update(self, delta_time: float) -> None:
        self.__current_wave.update()
        if self.__current_wave.get_finished():
            self.__current_wave_index += 1
            if self.__current_wave_index >= len(self.__waves):
                self.__finished = True
                return
            self.__current_wave = self.__waves[self.__current_wave_index]

    def get_finished(self) -> bool:
        return self.__finished
