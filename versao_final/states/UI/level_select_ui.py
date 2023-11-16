from states.UI.ui import UI
from game import Game
from buttons.text_button import TextButton
import pygame
import states.in_game_state as in_game_state
class LevelSelectUI(UI):
    def __init__(self, context: Game) -> None:
        super().__init__(context)
        self.buttons = [ 
            TextButton(pygame.font.Font('assets/fonts/Pixeltype.ttf',25).render('Jogar',True,'black'),'green',pygame.Rect(200,700,50,20),lambda: context.change_state(in_game_state.InGameState(context)))
        ]
    def render(self, screen):
        pass