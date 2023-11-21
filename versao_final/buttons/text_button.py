import pygame
from buttons.button import Button
from typing import Callable

class TextButton(Button):
    def __init__(self, text: pygame.Surface, color: str, rect: pygame.Rect, action: Callable) -> None:
        super().__init__(color, rect, action)
        self.text = text
    def draw(self, screen):
        pygame.draw.rect(screen, self.get_color(), self.get_rect(),0,10)
        pygame.draw.rect(screen, 'black', self.get_rect(),3,10)
        #screen.blit(self.text, self.get_rect())
        screen.blit(self.text,self.text.get_rect(center=(self.get_rect().center)))