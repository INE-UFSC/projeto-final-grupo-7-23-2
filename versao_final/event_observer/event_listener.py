from abc import ABC, abstractmethod
import pygame


class EventListener(ABC):
    def __init__(self, interested_events: list[int]):
        self.__interested_events = interested_events

    @abstractmethod
    def on_event(self, event: pygame.event.Event):
        pass

    def interested_events(self):
        return self.__interested_events
