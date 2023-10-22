import pygame
from entities.entity import Entity
from entities.enemy import Enemy


class Tower(Entity):
    def __init__(self, position: pygame.Vector2, range: float, target: Enemy):
        Entity.__init__(self, position)
        self.__state = self.watching_target
        self.__range = range
        self.__target: Enemy = target
        self.__angle: float
        self.__vector = pygame.Vector2(0, 0)

    def watching_target(self) -> None:
        if self.get_position().distance_to(self.__target.get_position()) < self.__range:
            self.__state = self.shooting_target

    def shooting_target(self) -> None:
        pass

    def update(self, delta_time: float) -> None:
        vector = self.get_position() - self.__target.get_position()
        vector.scale_to_length(50)
        self.__vector = vector

    def draw_at(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (255, 0, 0, 100), self.get_position(), self.__range, 2)
        pygame.draw.rect(screen, (0, 100, 230), pygame.Rect(self.get_position() - pygame.Vector2(20, 20), (40, 40)))
        pygame.draw.line(screen, (0, 255, 0), self.get_position(), self.get_position() - self.__vector, 3)
