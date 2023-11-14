from abc import ABC, abstractmethod
from buttons.button import Button
import game

class UI(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.buttons: list[Button]
    
    @abstractmethod
    def render(self):
        pass