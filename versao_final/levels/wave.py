import pygame

from entities.enemies.enemy import Enemy
from entities.enemies.bee import Bee
from entities.enemies.ogre import Ogre
from entities.enemies.wolf import Wolf
from path import Path


class EnemyData:
    def __init__(self, type: str, amount: int, delay: int, next_enemy_delay: int):
        self.type = type
        self.amount = amount
        self.delay = delay
        self.next_enemy_delay = next_enemy_delay


class Wave:
    def __init__(self, enemies_data: dict, enemies_ref: list[Enemy], path: Path, delay: int):
        self.__enemies_ref = enemies_ref
        self.__path = path

        self.__enemies_data: list[EnemyData] = []
        self.__delay = delay

        self.__last_time = pygame.time.get_ticks()
        self.__waiting = True
        self.__wait_time = 0
        self.__finished = False

        for enemy_data in enemies_data:
            self.__enemies_data.append(
                EnemyData(
                    enemy_data['type'],
                    enemy_data['amount'],
                    enemy_data['delay'] * 1000,
                    enemy_data['nextEnemyDelay']
                )
            )

        self.__current_enemy_index = 0
        self.__current_enemy_delay = self.__enemies_data[self.__current_enemy_index].delay
        self.__current_enemy_counter = 0

    def update(self) -> None:
        if self.__current_enemy_index >= len(self.__enemies_data):
            self.__finished = True
            return

        if not self.__waiting:
            if self.__current_enemy_counter > self.__enemies_data[self.__current_enemy_index].amount:
                self.__waiting = True
                self.__wait_time = self.__enemies_data[self.__current_enemy_index].next_enemy_delay
                self.__current_enemy_index += 1
                self.__current_enemy_counter = 0
                return

            else:
                enemy_type = self.__enemies_data[self.__current_enemy_index].type
                if enemy_type == 'Bee':
                    self.__enemies_ref.append(Bee(self.__path))
                elif enemy_type == 'Ogre':
                    self.__enemies_ref.append(Ogre(self.__path))
                elif enemy_type == 'Wolf':
                    self.__enemies_ref.append(Wolf(self.__path))

                self.__current_enemy_counter += 1
                self.__waiting = True
                self.__wait_time = self.__enemies_data[self.__current_enemy_index].delay

        # waiting
        else:
            if pygame.time.get_ticks() - self.__last_time > self.__wait_time:
                self.__waiting = False
                self.__last_time = pygame.time.get_ticks()

    def get_finished(self) -> bool:
        return self.__finished
