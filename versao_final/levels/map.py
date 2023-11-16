import pygame

from dao.map_dao import MapDAO
from drawable import Drawable


class Map(Drawable):
    def __init__(self):
        map_dao = MapDAO('assets/layouts/map_0/map_0.csv')
        map_layout = map_dao.read_data()

        tileset_image = pygame.image.load('assets/field/tiles/FieldsTileset.png')
        tile_amount_x = tileset_image.get_size()[0] // 32
        tile_amount_y = tileset_image.get_size()[1] // 32

        tileset: list[pygame.Surface] = []
        for row in range(tile_amount_x):
            for col in range(tile_amount_y):
                tileset.append(tileset_image.subsurface(col * 32.0, row * 32.0, 32.0, 32.0))

        self.__map_array: list[list[pygame.Surface]] = []
        for line in map_layout:
            self.__map_array.append([tileset[tile] for tile in line])

    def draw_at(self, screen: pygame.Surface) -> None:
        for i, row in enumerate(self.__map_array):
            for j, tile in enumerate(row):
                screen.blit(tile, (j * 32, i * 32))

