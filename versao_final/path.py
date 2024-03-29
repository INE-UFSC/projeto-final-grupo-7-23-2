import pygame

from drawable import Drawable


# path é drawable, mas apenas temporariamente, para poder testar
class Path(Drawable):
    def __init__(self, points: list[pygame.Vector2], margin: int) -> None:
        if len(points) == 0:
            raise ValueError('Path must have at least one point')

        self.__points = points

    def draw_at(self, screen: pygame.Surface) -> None:
        for start, end in zip(self.get_points(), self.get_points()[1:]):
            pygame.draw.line(screen, (60, 60, 60), start, end, 5)

    def get_points(self) -> list[pygame.Vector2]:
        return self.__points.copy()

    def get_start(self) -> pygame.Vector2:
        return self.get_points()[0]

    def get_end(self) -> pygame.Vector2:
        return self.get_points()[-1]

