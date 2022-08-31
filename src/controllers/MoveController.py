import os
from shutil import move
from datetime import datetime


class MoveController:
    def __init__(self, file_name: str, path: str) -> None:
        self.__file_name: str = file_name
        self.__path: str = path
        self.year = datetime.now().year
        self.mouth = datetime.now().month
        match self.mouth:
            case 1:
                self.mouth: str = "jan"
            case 2:
                self.mouth: str = "fev"
            case 3:
                self.mouth: str = "mar"
            case 4:
                self.mouth: str = "abr"
            case 5:
                self.mouth: str = "mai"
            case 6:
                self.mouth: str = "jun"
            case 7:
                self.mouth: str = "jul"
            case 8:
                self.mouth: str = "ago"
            case 9:
                self.mouth: str = "set"
            case 10:
                self.mouth: str = "out"
            case 11:
                self.mouth: str = "nov"
            case 12:
                self.mouth: str = "dez"

    @property
    def file_name(self) -> str:
        return self.__file_name

    @property
    def path(self) -> str:
        return self.__path

    def __createDir(self) -> None:
        """ Cria um diretorio com o ano e mes"""
        os.chdir(self.path)
        try:
            if self.year in os.listdir(self.path):
                if self.mouth not in os.listdir(self.path + "\\" + str(self.year)):
                    os.mkdir(self.path + str(self.year) + "\\" + str(self.mouth))
            else:
                os.mkdir(self.path + str(self.year))
                os.mkdir(self.path + str(self.year) + "\\" + str(self.mouth))
        except FileExistsError as e:
            print(e)

    def move(self) -> None:
        """
        Move os arquivos identificados para a pasta
        da data/ mes atual
        """
        self.__createDir()
        move(self.path + self.file_name, self.path + str(self.year) + "\\" + str(self.mouth) + "\\" + self.file_name)
        print(self.path+ self.file_name)
