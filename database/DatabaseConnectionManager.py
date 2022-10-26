from utils.Logging import Logging


class DatabaseConnectionManager:
    def __init__(self, logger, config):
        self.logger = logger
        self.configManager = config
        self.config = self.configManager.getConfig()
        self.database = None
        self.logger.debug("Database Manager __init__")
        self.setup()

    def setup(self):
        self.logger.info(f"Trying to Load Database Connection Type: {self.config['database']['type']}")

        type = str(self.config['database']['type']).lower()

        if type == "mysql":
            from database.types.MysqlDatabase import MysqlDatabase
            self.database = MysqlDatabase(Logging("Mysql"), self.configManager)
        elif type == "sqlite":
            pass
        else:
            self.logger.error('No implemented database type specified')

    def getDatabase(self):
        return self.database
