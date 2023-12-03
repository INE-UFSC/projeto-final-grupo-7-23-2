from __future__ import annotations
import pygame

import states.state as state
import game

from levels.map import Map
from entities.enemies.wolf import Wolf
from entities.tower import Tower
from entities.projectile import Projectile
from entities.player_base import PlayerBase
from shop import Shop
from buttons.text_button import TextButton
from singletons.constants import Constants as C
import states.game_over_state as game_over_state


class InGameState(state.State):
    def __init__(self, context: game.Game, level_number: int):
        # FIX: alterar menuUI para ingameUI quando for criado
        state.State.__init__(self, context )

        self.__map = Map(level_number)
        path = self.__map.get_path()
        self.__player_base = PlayerBase(path.get_end() + pygame.Vector2(40, 0))
        self.__enemy = Wolf(path)

        self.__projectiles: list[Projectile] = []
        self.__towers: list[Tower] = []
        self.__shop = Shop(self, 100 * (level_number + 1))
        self.__place_tower = False

        self.__paused = False

        width = C().get_screen_width()
        height = C().get_screen_height()

        click_sound = pygame.mixer.Sound(C().get_sound('basic_click.wav'))
        buy_sound = pygame.mixer.Sound(C().get_sound('buy_sound.wav'))
        upgrade_sound = pygame.mixer.Sound(C().get_sound('upgrade_sound.wav'))

        self.buttons = [
            TextButton(pygame.font.Font(C().get_font('Pixeltype.ttf'),13).render('Comprar($XX)', True, 'black'),'#D9D9D9', width/25, height/4.6, width/15, height/35, buy_sound, lambda: self.buy_tower()), #COMPRAR TORRE 1
            TextButton(pygame.font.Font(C().get_font('Pixeltype.ttf'),13).render('Aprimorar($XX)', True, 'black'),'#D9D9D9', width/25, height/4, width/15, height/35, upgrade_sound, lambda: self.__shop.upgrade()), #APRIMORAR TORRE 1
            TextButton(pygame.font.Font(C().get_font('Pixeltype.ttf'),13).render('Comprar($XX)', True, 'black'),'#D9D9D9', width/8, height/4.6, width/15, height/35, buy_sound, lambda: self.buy_tower()), #COMPRAR TORRE 2
            TextButton(pygame.font.Font(C().get_font('Pixeltype.ttf'),13).render('Aprimorar($XX)', True, 'black'),'#D9D9D9', width/8, height/4, width/15, height/35, upgrade_sound, lambda: self.__shop.upgrade()), #APRIMORAR TORRE 2
            TextButton(pygame.font.Font(C().get_font('Pixeltype.ttf'),13).render('Pausa', True, 'black'),'#FF5C00', width/5, height/4.6, width/15, height/35, click_sound, lambda: self.pause()), #PAUSAR
            TextButton(pygame.font.Font(C().get_font('Pixeltype.ttf'),13).render('Desistir', True, 'black'),'#FF0000', width/5, height/4, width/15, height/35, click_sound, lambda: context.change_state(game_over_state.GameOverState(context))) #DESISTIR
        ]
        self.shop_title = pygame.font.Font(C().get_font('Pixeltype.ttf'),40).render('Loja',True, 'black')
        self.total_money = pygame.font.Font(C().get_font('Pixeltype.ttf'), 35).render('$1000',True, 'black')

    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.get_ctx().exit_game()
                elif event.key == pygame.K_p:
                    print(self.__shop.get_money())
                    self.buy_tower()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    if self.__place_tower and not self.__paused:
                        position = pygame.mouse.get_pos()
                        self.__towers.append(self.__shop.add_tower(self.__enemy, position))
                        self.__place_tower = False
                    self.check_buttons(pygame.mouse.get_pos())

                elif event.button == pygame.BUTTON_RIGHT:
                    self.__tower_factory.upgrade()

            elif event.type == pygame.QUIT:
                self.get_ctx().exit_game()

    def update(self, delta_time: float) -> None:
        if not self.__paused:
            self.__enemy.update(delta_time)
            for tower in self.__towers:
                tower.update(delta_time)

            for projectile in self.__projectiles:
                projectile.update(delta_time)
                if projectile.get_position().distance_to(self.__enemy.get_position()) < 10:
                    self.__projectiles.remove(projectile)
                    self.__enemy.take_damage(projectile.get_damage())
                # if not self.enemy.is_alive():
                #     print('inimigo morreu')
                #     pygame.quit()
                #     sys.exit()

        # if self.__place_tower:
        #     self.__place_tower = False
        #     new_tower = Tower(pygame.Vector2(pygame.mouse.get_pos()), 250, self.__enemy, 50, self.__projectiles)
        #     self.__towers.append(new_tower)
        #     self.__drawables.append(new_tower)

        # if self.enemy.finished_path():
        #     print('inimigo chegou na base')
        #     pygame.quit()
        #     sys.exit()

    def render(self) -> None:
        screen = self.get_ctx().get_screen()

        self.__map.draw_at(screen)

        for tower in self.__towers:
            tower.draw_at(screen)

        self.__enemy.draw_at(screen)
        self.__player_base.draw_at(screen)

        for projectile in self.__projectiles:
            projectile.draw_at(screen)
        
        self.draw_at(screen)
    
    def draw_at(self, screen: pygame.Surface):
        #constantes dimensionais
        width = C().get_screen_width()
        height = C().get_screen_height()

        pygame.draw.rect(screen, '#A3A3A3',pygame.Rect(0,0, width/4, height/3.5), border_bottom_right_radius=10) #retângulo maior
        pygame.draw.rect(screen, 'black',pygame.Rect(0,0, width/4, height/3.5), 3, border_bottom_right_radius=10 ) #contorno do círculo maior

        screen.blit(self.shop_title, self.shop_title.get_rect(center=(width/8, height/30)))
        screen.blit(self.total_money, self.total_money.get_rect(center=(width/5, height/8)))

        pygame.draw.circle(screen, '#D9D9D9', (width/25, height/8), 37.5) #círculo 1
        pygame.draw.circle(screen, 'black', (width/25, height/8), 37.5, 2) #contorno do círculo 1

        pygame.draw.circle(screen, '#D9D9D9', (width/8, height/8), 37.5) #círculo 2
        pygame.draw.circle(screen, 'black', (width/8, height/8), 37.5, 2) #contorno do círculo 2

        for button in self.buttons:
            button.draw_at(screen)
    
    def buy_tower(self):
        if self.__shop.can_buy_tower():
            self.__shop.buy_tower()
            self.__place_tower = True
    
    def pause(self):
        self.__paused = not self.__paused
    
    def get_projectiles(self) -> list[Projectile]:
        return self.__projectiles
    