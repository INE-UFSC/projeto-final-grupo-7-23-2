import pygame


class Path:
    def __init__(self, points: list[pygame.Vector2]) -> None:
        self.__points = points
        self.__margin = 15

    def draw_at(self, screen: pygame.Surface) -> None:
        for start, end in zip(self.get_points(), self.get_points()[1:]):
            pygame.draw.line(screen, (0, 0, 255), start, end, 5)

    def get_points(self) -> list[pygame.Vector2]:
        return self.__points.copy()

    def get_start(self) -> pygame.Vector2:
        return self.get_points()[0]

    def get_end(self) -> pygame.Vector2:
        return self.get_points()[-1]

    def get_margin(self) -> float:
        return self.__margin

