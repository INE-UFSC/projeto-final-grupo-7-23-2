from __future__ import annotations

from typing import Callable
import pygame

from event_observer.event_listener import EventListener


class EventManager:
    def __init__(self):
        self.__listeners: dict[pygame.event.EventType, set[EventListener]] = {}

    def subscribe(self, event_type: pygame.event.EventType, listener: EventListener) -> None:
        self.__listeners[event_type].add(listener)

    def unsubscribe(self, event_type: pygame.event.EventType, listener: EventListener) -> None:
        self.__listeners[event_type].remove(listener)

    def notify(self, event: pygame.event.Event) -> None:
        if event.type in self.__listeners:
            for listener in self.__listeners[event.type]:
                listener.notify(event):

    def handle_event(self) -> None:

