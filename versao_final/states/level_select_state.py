from states.state import State
from versao_final.states.UI.ui import UI

class LevelSelectState(State):
    def __init__(self, context, UI: UI):
        super().__init__(context, UI)