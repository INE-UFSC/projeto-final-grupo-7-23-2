from __future__ import annotations
import pygame
from states.UI.ui import UI
import game
from buttons.text_button import TextButton
from singletons.constants import Constants as C

class InGameUI(UI):
    def __init__(self, context: game.Game) -> None:
        super().__init__(context)
        width = C().get_screen_width()
        height = C().get_screen_height()
        self.buttons = [
            TextButton(pygame.font.Font(C().get_font('Pixeltype.ttf'),13).render('Comprar($XX)', True, 'black'),'#D9D9D9', width/25, height/4.6, width/15, height/35, lambda: print(1)), #COMPRAR TORRE 1
            TextButton(pygame.font.Font(C().get_font('Pixeltype.ttf'),13).render('Aprimorar($XX)', True, 'black'),'#D9D9D9', width/25, height/4, width/15, height/35, lambda: print(2)), #APRIMORAR TORRE 1
            TextButton(pygame.font.Font(C().get_font('Pixeltype.ttf'),13).render('Comprar($XX)', True, 'black'),'#D9D9D9', width/8, height/4.6, width/15, height/35, lambda: print(3)), #COMPRAR TORRE 2
            TextButton(pygame.font.Font(C().get_font('Pixeltype.ttf'),13).render('Aprimorar($XX)', True, 'black'),'#D9D9D9', width/8, height/4, width/15, height/35, lambda: print(4)), #APRIMORAR TORRE 2
            TextButton(pygame.font.Font(C().get_font('Pixeltype.ttf'),13).render('Pausa', True, 'black'),'#FF5C00', width/5, height/4.6, width/15, height/35, lambda: print(5)), #PAUSAR
            TextButton(pygame.font.Font(C().get_font('Pixeltype.ttf'),13).render('Desistir', True, 'black'),'#FF0000', width/5, height/4, width/15, height/35, lambda: print(6)), #DESISTIR
        ]
        self.shop_title = pygame.font.Font(C().get_font('Pixeltype.ttf'),40).render('Loja',True, 'black')
        self.total_money = pygame.font.Font(C().get_font('Pixeltype.ttf'), 35).render('$1000',True, 'black')
    
    def draw_at(self, screen: pygame.Surface) -> None:

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