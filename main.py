from utils.Logging import Logging
from database.DatabaseConnectionManager import DatabaseConnectionManager
from utils.configManager import ConfigManager

DEBUG = False

if __name__ == '__main__':
    logger = Logging()
    config = ConfigManager(logger)

    # test logging
    if DEBUG:
        logger.info("test info")
        logger.error("test error")
        logger.debug("test debug")


    # test database insert, select, update, delete
    database = DatabaseConnectionManager(logger, config)

