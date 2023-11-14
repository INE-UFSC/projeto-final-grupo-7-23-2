from __future__ import annotations
from abc import ABC, abstractmethod
from buttons.button import Button
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

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def change_state(self, new_state):
        pass

    def check_buttons(self, mouse_pos): #the Game class will give us the mouse position upon calling this function
        for button in self.buttons:
            if button.get_rect().collidepoint(mouse_pos):
                button.activate()