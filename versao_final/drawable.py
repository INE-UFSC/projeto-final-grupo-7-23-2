from abc import ABC, abstractmethod

import pygame


class Drawable(ABC):
    @abstractmethod
    def draw_at(self, screen: pygame.Surface):
        pass
