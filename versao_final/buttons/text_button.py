import pygame
from buttons.button import Button
from typing import Callable

class TextButton(Button):
    def __init__(self, text: pygame.Surface, color: str, centerx, centery, width: int, height: int, sound, action: Callable) -> None:
        super().__init__(color, centerx, centery, width, height, sound, action)
        self.text = text

    def draw_at(self, screen):
        pygame.draw.rect(screen, self.get_color(), self.get_rect(),0,10)
        pygame.draw.rect(screen, 'black', self.get_rect(),3,10) #borda do botão
        #screen.blit(self.text, self.get_rect())
        screen.blit(self.text, self.text.get_rect(center=(self.get_rect().center)))

