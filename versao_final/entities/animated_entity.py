import pygame
from entities.entity import Entity
from animation import Animation

class AnimatedEntity(Entity):
    def __init__(self, position: pygame.Vector2, images:list[pygame.Surface], fps: int):
        super().__init__(position)
        self.__animation = Animation(images, fps)

    def draw_at(self, screen: pygame.Surface):
        screen.blit(self.__animation.get_current_image(), self.get_position())
    
    def update(self):
        self.__animation.update()

    def get_animation(self):
        return self.__animation

