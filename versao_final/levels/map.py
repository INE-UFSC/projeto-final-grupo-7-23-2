import pygame
import json

from drawable import Drawable
from path import Path

from singletons.constants import Constants as C


class Map(Drawable):
    def __init__(self, map_number: int):
        path_object = f'assets/layouts/map_{map_number}/map_{map_number}.tmj'

        with open(path_object, 'r') as file:
            map_dict = json.load(file)

        layout = map_dict['layers'][0]['data']
        layout_width = map_dict['layers'][0]['width']
        layout_height = map_dict['layers'][0]['height']

        path_object = map_dict['layers'][1]['objects'][0]['polyline']
        path_origin_x = map_dict['layers'][1]['objects'][0]['x']
        path_origin_y = map_dict['layers'][1]['objects'][0]['y']
        path_points: list[pygame.Vector2] = []
        for point in path_object:
            path_points.append(pygame.Vector2(path_origin_x + point['x'], path_origin_y + point['y']))

        self.__map_path = Path(path_points, 15)
        tileset_image = pygame.image.load('assets/field/tiles/FieldsTileset.png')
        tile_amount_x = tileset_image.get_size()[0] // 32
        tile_amount_y = tileset_image.get_size()[1] // 32

        tileset: list[pygame.Surface] = []
        for row in range(tile_amount_x):
            for col in range(tile_amount_y):
                tileset.append(tileset_image.subsurface(col * 32.0, row * 32.0, 32.0, 32.0))

        # TODO: criar uma classe Tile
        self.__tile_array: list[list[pygame.Surface]] = [[None for __ in range(layout_width)] for _ in range(layout_height)]
        for i, tile in enumerate(layout):
            line_number = i // layout_width
            column_number = i % layout_width
            self.__tile_array[line_number][column_number] = tileset[tile - 1]

    def draw_at(self, screen: pygame.Surface) -> None:
        size = C().get_tile_size()
        for i, row in enumerate(self.__tile_array):
            for j, tile in enumerate(row):
                tile = pygame.transform.scale(tile, (size, size))
                screen.blit(tile, (j * size, i * size))

    def get_path(self) -> Path:
        return self.__map_path
