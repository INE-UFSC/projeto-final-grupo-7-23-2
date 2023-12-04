import pygame
from entities.entity import Entity
from animation import Animation

class AnimatedEntity(Entity):
    def __init__(self, position: pygame.Vector2, image_paths:list[str], fps: int):
        super().__init__(position)
        self.__images: list[pygame.Surface] = []
        for path in image_paths:
            self.__images.append(pygame.transform.flip(pygame.transform.scale2x(pygame.image.load(path).convert_alpha()), True, False))
        self.__animation = Animation(self.__images, fps)

    def draw_at(self, screen: pygame.Surface):
        screen.blit(self.__animation.get_current_image(), self.get_position())

    def update(self):
        self.__animation.update()

    def get_animation(self):
        return self.__animation

