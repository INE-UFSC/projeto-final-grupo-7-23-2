import pygame

from entities.entity import Entity


class PlayerBase(Entity):
    def __init__(self, position: pygame.Vector2):
        Entity.__init__(self, position)
        self.__size = 80

    def update(self, delta_time: float) -> None:
        return

    def draw_at(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, (0, 50, 255), pygame.Rect(self.get_position() - pygame.Vector2(self.__size / 2, self.__size / 2), (self.__size, self.__size)))

    def get_size(self) -> int:
        return self.__size
