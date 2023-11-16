from __future__ import annotations
from abc import ABC, abstractmethod
from states.UI.ui import UI

class State(ABC):
    def __init__(self, context, UI: UI):
        self.__context = context
        self.UI = UI
        self.buttons = UI.buttons

    def get_ctx(self):
        return self.__context

    @abstractmethod
    def update(self, delta_time: float):
        pass


    def render(self):
        self.UI.render(self.get_ctx().get_screen())

    def check_buttons(self, mouse_pos): #the Game class will give us the mouse position upon calling this function
        for button in self.buttons:
            if button.get_rect().collidepoint(mouse_pos):
                button.activate()
                return