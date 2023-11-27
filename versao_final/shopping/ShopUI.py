from states.UI.ui import UI
from versao_final.game import Game
import pygame
from buttons.text_button import TextButton
from factories.tower_factory import Tower_Factory
from singletons.constants import Constants as C

class ShopUI(UI):
    def __init__(self, context: Game) -> None:
        super().__init__(context)
        self.buttons = [TextButton(C().get_font('Pixeltype.ttf').render('Comprar($50)',True,'black'),'green',pygame.Rect (850,150,90,40),print())]
        self.buttons = [TextButton(C().get_font('Pixeltype.ttf').render('Aprimorar($50)',True,'black'),'#FFD700',pygame.Rect (850,150,90,40),print())]
        self.factory = Tower_Factory()
    
    def render(self,screen):
        shop_rect = pygame.Rect(800,0,400,500)
        pygame.draw.rect(screen,'#89cff0',shop_rect)