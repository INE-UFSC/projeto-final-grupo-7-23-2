from shopping.shop_ui import ShopUI
from game import Game
from factories.tower_factory import TowerFactory

class Shop:
    def __init__(self, context: Game, ui: ShopUI) -> None:
        self.__context = context
        self.ui = ui
        self.__buttons = ui.buttons
        self.__factory = TowerFactory