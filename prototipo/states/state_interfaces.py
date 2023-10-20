from __future__ import annotations
from abc import ABC, abstractmethod


class Context(ABC):
    def __init__(self, initial_state: 'State'):
        self.__state = initial_state

    def change_state(self, new_state: 'State') -> None:
        self.__state = new_state

    def get_state(self) -> 'State':
        return self.__state

class State(ABC):
    def __init__(self, context: 'Context'):
        self.__context = context

    def get_ctx(self) -> 'Context':
        return self.__context

    @abstractmethod
    def update(self):
        pass
