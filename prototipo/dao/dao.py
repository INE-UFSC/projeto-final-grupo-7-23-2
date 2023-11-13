from abc import ABC, abstractmethod


class DAO(ABC):
    def __init__(self, path: str):
        self.__path = path

    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def write_data(self):
        pass

    def get_path(self):
        return self.__path
