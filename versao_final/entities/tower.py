import pygame

from entities.entity import Entity
from entities.enemies.enemy import Enemy
from entities.projectile import Projectile
from singletons.constants import Constants as C


class Tower(Entity):
    def __init__(self, position: pygame.Vector2, range: float, target: Enemy, damage: float, shoot_rate: float, bullets_list: list[Projectile]):
        Entity.__init__(self, position)
        self.__state = self.watching_target
        self.__range = range
        self.__target: Enemy = target
        self.__shoot_rate = shoot_rate
        self.__damage = damage
        self.__bullets_list = bullets_list
        self.__angle: float
        self.__aim_vector = pygame.Vector2(0, 0)
        self.__last_shoot = 0.0
        self.build_sound = pygame.mixer.Sound(C().get_sound('build_tower.wav'))
        self.build_sound.play()

    def watching_target(self) -> None:
        if self.get_position().distance_to(self.__target.get_position()) < self.__range:
            self.__state = self.shooting_target

    def shooting_target(self) -> None:
        if self.get_position().distance_to(self.__target.get_position()) > self.__range:
            self.__state = self.watching_target

        current_time = pygame.time.get_ticks()
        if current_time - self.__last_shoot > (1 / self.__shoot_rate) * 1000:
            print('atirando')
            self.__bullets_list.append(Projectile(self.get_position() - self.__aim_vector, self.__target, self.__damage))
            self.__last_shoot = current_time

    def update(self, delta_time: float) -> None:
        vector = self.get_position() - self.__target.get_position()
        vector.scale_to_length(50)
        self.__aim_vector = vector
        self.__state()

    def draw_at(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (255, 0, 0, 100), self.get_position(), self.__range, 2)
        pygame.draw.rect(screen, (0, 100, 230), pygame.Rect(self.get_position() - pygame.Vector2(20, 20), (40, 40)))
        pygame.draw.line(screen, (0, 255, 0), self.get_position(), self.get_position() - self.__aim_vector/2, 3)
