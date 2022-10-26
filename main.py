import time

from utils.Logging import Logging
from database.DatabaseConnectionManager import DatabaseConnectionManager
from utils.configManager import ConfigManager

DEBUG = False

if __name__ == '__main__':
    main_logger = Logging("Main")
    config = ConfigManager(Logging("ConfigManager"))

    # test logging
    if DEBUG:
        main_logger.info("test info")
        main_logger.error("test error")
        main_logger.debug("test debug")

    # test database insert, select, update, delete
    database = DatabaseConnectionManager(Logging("DatabaseManager"), config)

    main_logger.info("while loop started")
    while True:
        time.sleep(0.005)
        pass
