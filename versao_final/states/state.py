from __future__ import annotations

from abc import ABC, abstractmethod
from buttons.button import Button
import game


class State(ABC):
    def __init__(self, context: game.Game):
        self.__context = context
        self.buttons = list[Button]

    def get_ctx(self):
        return self.__context

    @abstractmethod
    def update(self, delta_time: float):
        pass

    def render(self):
        self.draw_at(self.get_ctx().get_screen())
    
    @abstractmethod
    def draw_at(self):
        pass

    def check_buttons(self, mouse_pos): #the Game class will give us the mouse position upon calling this function
        for button in self.buttons:
            if button.get_rect().collidepoint(mouse_pos):
                button.handle_click()
                return
