import pygame
from entities.enemy import Enemy


class Game:
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)

        self.__is_running = True

        self.enemy = Enemy(pygame.Vector2(100, 100))

    def run(self):
        clock = pygame.time.Clock()

        while self.__is_running:
            delta_time = clock.tick() / 1000.0
            self.update(delta_time)
            self.render()
            clock.tick(60)

    def update(self, delta_time: float = 0.0):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    self.set_is_running(False)
            #
            #     elif event.key == pygame.K_w:
            #         self.enemy.move_up()
            #
            #     elif event.key == pygame.K_d:
            #         self.enemy.move_right()
            #
            #     elif event.key == pygame.K_s:
            #         self.enemy.move_down()
            #
            #     elif event.key == pygame.K_a:
            #         self.enemy.move_left()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            self.enemy.move_up()

        if keys_pressed[pygame.K_d]:
            self.enemy.move_right()

        if keys_pressed[pygame.K_s]:
            self.enemy.move_down()

        if keys_pressed[pygame.K_a]:
            self.enemy.move_left()

    def render(self):
        self.__screen.fill((0, 0, 0))
        self.enemy.draw_at(self.__screen)
        pygame.display.flip()

    def set_is_running(self, is_running: bool) -> None:
        self.__is_running = is_running

    def get_screen(self) -> pygame.Surface:
        return self.__screen

