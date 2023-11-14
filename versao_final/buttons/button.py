import pygame
from abc import ABC, abstractmethod
screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
from typing import Callable

class Button(ABC):
    def __init__(self,  color: str, rect: pygame.Rect, action: Callable) -> None:
        self.__color = color
        self.__rect = rect
        self.__action = action
    
    def get_rect(self):
        return self.__rect
    
    @abstractmethod
    def draw(self):
        pass
    
    def activate(self):
        self.__action()