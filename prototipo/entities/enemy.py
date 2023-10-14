import pygame
from entities.entity import Entity

class Enemy(Entity):
    def __init__(self, position: pygame.Vector2):
        Entity.__init__(self, position)
        self.__speed = 5

    def update(self) -> None: ...

    def move_up(self) -> None:
        self.set_position(self.get_position() + pygame.Vector2(0, -self.__speed))

    def move_right(self) -> None:
        self.set_position(self.get_position() + pygame.Vector2(self.__speed, 0))

    def move_down(self) -> None:
        self.set_position(self.get_position() + pygame.Vector2(0, self.__speed))

    def move_left(self) -> None:
        self.set_position(self.get_position() + pygame.Vector2(-self.__speed, 0))

    def draw_at(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (255, 0, 0), self.get_position(), 10)
