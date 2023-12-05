import pygame

class Animation:
    def __init__(self, images: list[pygame.Surface], fps: int) -> None:
        self.__images = images
        self.__current_image_index = 0
        self.__last_image_time = 0
        self.__fps = fps

    def update(self) -> None:
        current_time = pygame.time.get_ticks()
        if current_time - self.__last_image_time > 1000 / self.__fps:
            self.__current_image_index += 1
            self.__current_image_index %= len(self.__images)
            self.__last_image_time = current_time

    def get_current_image(self) -> pygame.Surface:
        return self.__images[self.__current_image_index]

    def change_animation(self, sprites: list[pygame.Surface]):
        self.__images = sprites
        self.__current_image_index = 0

    def flip(self, flip_horizontally, flip_vertically):
        for i in range(len(self.__images)):
            self.__images[i] = pygame.transform.flip(self.__images[i], flip_horizontally, flip_vertically)

