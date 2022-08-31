from getpass import getuser
#from src.models.Monitor import Monitor
from models.Monitor import Monitor


if __name__ == '__main__':
    path = f"C:\\Users\\{getuser()}\\Desktop\\"
    monitor_debug = Monitor(path)
    monitor_debug.monitoring()
