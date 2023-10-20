from __future__ import annotations
from abc import ABC, abstractmethod

from game import Game

class State(ABC):
    def __init__(self, context: Game):
        self.__context = context

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def handle_input(self):
        pass
