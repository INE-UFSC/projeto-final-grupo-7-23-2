from __future__ import annotations
from abc import ABC, abstractmethod

import game

class State(ABC):
    def __init__(self, context: game.Game):
        self.__context = context

    def get_ctx(self) -> game.Game:
        return self.__context

    @abstractmethod
    def handle_input(self) -> None:
        pass

    @abstractmethod
    def update(self, delta_time: float):
        pass

    @abstractmethod
    def render(self):
        pass

