#from src.controllers.MoveController import MoveController
from controllers.MoveController import MoveController

class Move:
    def __init__(self, file_name: str, path: str) -> None:
        self.__file_name: str = file_name
        self.__path: str = path

    @property
    def file_name(self) -> str:
        return self.__file_name

    @property
    def path(self) -> str:
        return self.__path

    def __str__(self) -> str:
        return self.file_name

    def __repr__(self) -> str:
        return self.file_name

    def run(self) -> None:
        """
        Move o arquivo identificado
        para as pastas do mês / ano vigente
        :return:
        """
        move = MoveController(file_name=self.file_name, path=self.path)
        move.move()
