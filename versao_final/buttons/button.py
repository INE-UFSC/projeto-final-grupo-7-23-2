import pygame
from abc import ABC, abstractmethod
from typing import Callable

class Button(ABC):
    def __init__(self,  color: str, centerx, centery, width: int, height: int, sound: pygame.mixer.Sound, action: Callable = lambda: None) -> None:
        self.__color = color
        self.__rect = pygame.Rect(0, 0, width, height)
        self.__rect.center = (centerx, centery)
        self.__sound = sound
        self.__action = action

    def get_rect(self) -> pygame.Rect:
        return self.__rect

    def get_color(self) -> str:
        return self.__color

    @abstractmethod
    def draw_at(self, screen: pygame.Surface) -> None:
        pass

    def handle_click(self) -> None:
        self.__action()
        self.__sound.play()
