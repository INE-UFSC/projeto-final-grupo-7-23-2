from singletons.singleton import Singleton

class Constants(Singleton):
    def __init__(self) -> None:
        self.__width = 1280
        self.__height = 720
        self.__tile_size = 40

    def get_level_path(self, level: int) -> str:
        return f'levels/level_{level}/'

    def get_screen_size(self):
        return (self.__width, self.__height)

    def get_font(self,font):
        return f'assets/fonts/{font}'
    
    def get_sound(self, sound):
        return f'assets/sounds/{sound}'

    def get_screen_width(self):
        return self.__width

    def get_screen_height(self):
        return self.__height

    def get_tile_size(self) -> float:
        return self.__tile_size
