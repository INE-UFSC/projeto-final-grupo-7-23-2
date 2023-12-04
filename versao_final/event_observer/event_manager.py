from __future__ import annotations

import sys
from typing import Callable
import pygame

from event_listener import EventListener


class EventManager:
    def __init__(self):
        self.__listeners: dict[int, set[EventListener]] = {}

    def subscribe(self, event_type: int, listener: EventListener) -> None:
        if event_type not in self.__listeners:
            self.__listeners[event_type] = set()

        self.__listeners[event_type].add(listener)

    def unsubscribe(self, event_type: int, listener: EventListener) -> None:
        if event_type in self.__listeners:
            self.__listeners[event_type].remove(listener)

    def notify(self, event: pygame.event.Event) -> None:
        if event.type in self.__listeners:
            for listener in self.__listeners[event.type]:
                listener.on_event(event)

    def handle_event(self) -> None:
        for event in pygame.event.get():
            self.notify(event)

class KeyBoardListener(EventListener):
    def __init__(self):
        EventListener.__init__(self, [pygame.KEYDOWN, pygame.KEYUP])

    def on_event(self, event: pygame.event.Event) -> None:
        quit = False
        if event.type == pygame.KEYDOWN:
            print("Key pressed")
            if event.key == pygame.K_ESCAPE:
                quit = True

        elif event.type == pygame.KEYUP:
            print("Key released")

        print(pygame.key.name(event.key))

        if quit:
            pygame.quit()
            sys.exit()

event_manager = EventManager()
keyboard_listener = KeyBoardListener()
for event_type in keyboard_listener.interested_events():
    event_manager.subscribe(event_type, keyboard_listener)

screen = pygame.display.set_mode((640, 480))
while True:
    event_manager.handle_event()
