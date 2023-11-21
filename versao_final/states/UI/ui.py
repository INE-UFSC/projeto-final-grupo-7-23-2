from __future__ import annotations

import pygame

from abc import ABC, abstractmethod
from buttons.button import Button

import game

class UI(ABC):
    def __init__(self, context: game.Game) -> None:
        super().__init__()
        self.buttons: list[Button]
        self.__context = context

    def get_ctx(self):
        return self.__context

    @abstractmethod
    def draw_at(self, screen: pygame.Surface) -> None:
        pass
