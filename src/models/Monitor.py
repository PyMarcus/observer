from typing import TypeVar
from getpass import getuser
#from src.controllers.MonitorController import MonitorController
from controllers.MonitorController import MonitorController


T = TypeVar("T")


class Monitor:
    def __init__(self, path: str) -> None:
        self.__path: str = path
        self.__monitor: T = MonitorController(self.path)

    @property
    def path(self) -> str:
        return self.__path

    @property
    def monitor(self) -> T:
        return self.__monitor

    def __str__(self) -> str:
        return self.path

    def __repr__(self) -> str:
        return self.path

    def monitoring(self) -> None:
        """
        Monitora eventos do desktop
        :return: None
        """
        self.monitor.run()


if __name__ == '__main__':
    path = f"C:\\Users\\{getuser()}\\Desktop\\"
    monitor_debug = Monitor(path)
    monitor_debug.monitoring()
