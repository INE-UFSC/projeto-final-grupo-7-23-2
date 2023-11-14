import pygame
from buttons.button import Button
from typing import Callable

class TextButton(Button):
    def __init__(self, color: str, rect: pygame.Rect, action: Callable) -> None:
        super().__init__(color, rect, action)