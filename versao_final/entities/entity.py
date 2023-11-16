import pygame

from abc import abstractmethod

from drawable import Drawable


class Entity(Drawable):
    def __init__(self, position: pygame.Vector2):
        self.__position = position

    def get_position(self) -> pygame.Vector2:
        return self.__position

    def set_position(self, position: pygame.Vector2) -> None:
        self.__position = position

    @abstractmethod
    def update(self):
        pass
