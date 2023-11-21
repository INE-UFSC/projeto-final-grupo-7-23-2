import pygame
from abc import ABC, abstractmethod
from typing import Callable

class Button(ABC):
    def __init__(self,  color: str, rect: pygame.Rect, action: Callable) -> None:
        self.__color = color
        self.__rect = rect
        self.__action = action
    
    def get_rect(self):
        return self.__rect
    
    def get_color(self):
        return self.__color
    
    @abstractmethod
    def draw_at(self, screen):
        pass
    
    def activate(self):
        self.__action()
