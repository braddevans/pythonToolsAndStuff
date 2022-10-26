import time

from Handlers.MainMenuHandler import MainMenuHandler
from Handlers.ProductMenuHandler import ProductMenuHandler
from utils.Logging import Logging
from database.DatabaseConnectionManager import DatabaseConnectionManager
from utils.configManager import ConfigManager

DEBUG = False

if __name__ == '__main__':
    main_logger = Logging("Main")
    config = ConfigManager(Logging("ConfigManager"))

    # test database insert, select, update, delete
    database = DatabaseConnectionManager(Logging("DatabaseManager"), config)

    main_logger.info("main loop started")

    will_exit = False
    menu = MainMenuHandler()

    while will_exit == False:
        time.sleep(0.005)
        print(menu)
        userinput = int(input("please input your option: "))
        if userinput == 0:
            will_exit = True
        elif userinput == 1:
            userinput = ProductMenuHandler(database.getDatabase())
        else:
            userinput = int(input("please input your option: "))

        pass
