import os
import time
import logging
#from src.models.Move import Move
from models.Move import Move
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


class MonitorController:
    def __init__(self, path: str) -> None:
        self.__path: str = path

    @property
    def path(self) -> str:
        return self.__path

    def run(self) -> None:
        """
            Monitora os eventos do path especificado,
            cada alteração pelo usuario será detectada
        """
        os.chdir(self.path)
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        event_handler = LoggingEventHandler()
        observer = Observer()
        observer.schedule(event_handler, self.path, recursive=False)
        observer.start()
        try:
            while True:
                for n in os.listdir(path=self.path):
                    if os.path.splitext(n)[1].strip() == ".xls" or os.path.splitext(n)[1].strip() == ".xlsx" or os.path.splitext(n)[1].strip() == ".xlm":
                        Move(file_name=n, path=self.path).run()
                time.sleep(1)  # o intervalo do monitoramento é de 1seg
        finally:
            observer.stop()
            observer.join()
