import pygame

from entities.entity import Entity
from path import Path

class Enemy(Entity):
    def __init__(self, path: Path):
        Entity.__init__(self, path.get_start())
        self.__path = path
        self.__state = "follow_path"
        self.__finished_path = False
        self.__health = 500
        self.__is_alive = True

        if len(self.__path.get_points()) < 2 :
            raise ValueError("Path must have at least two points")

        self.__current_point = self.__path.get_points()[1]
        self.__current_point_index = 1
        self.__speed = 100.0
        self.__velocity = pygame.Vector2(0, 0)
        self.__image: pygame.Surface

    def update(self, delta_time: float) -> None:
        if self.__state == "follow_path":
            self.follow_path(delta_time)

        elif self.__state == "idle":
            self.idle(delta_time)

        self.set_position(self.get_position() + self.get_velocity())

    def follow_path(self, delta_time: float) -> None:
        if self.get_position().distance_to(self.__current_point) < 1.5:
            if self.__current_point_index == len(self.__path.get_points()) - 1:
                self.__state = "idle"
                self.__finished_path = True
                return

            else:
                self.__current_point_index += 1
                self.__current_point = self.__path.get_points()[self.__current_point_index]

        self.set_velocity((self.__current_point - self.get_position()).normalize() * self.__speed * delta_time)
        self.set_position(self.get_position() + self.get_velocity())

    def idle(self, delta_time: float) -> None:
        self.__velocity = pygame.Vector2(0, 0)

    def draw_at(self, screen: pygame.Surface) -> None:
       screen.blit(self.get_image(), self.get_image().get_rect(center=self.get_position()))

    def get_velocity(self) -> pygame.Vector2:
        return self.__velocity

    def set_velocity(self, velocity: pygame.Vector2) -> None:
        self.__velocity = velocity

    def get_path(self) -> Path:
        return self.__path

    def finished_path(self) -> bool:
        return self.__finished_path

    def take_damage(self, damage: int) -> None:
        self.__health -= damage
        if self.__health <= 0:
            self.__is_alive = False

    def is_alive(self) -> bool:
        return self.__is_alive
    
    def get_image(self) -> pygame.Surface:
        return self.__image