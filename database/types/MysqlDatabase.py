import sys

import mysql.connector.pooling

class MysqlDatabase:
    def __init__(self, logger, config):
        self.logger = logger
        self.configManager = config
        self.config = self.configManager.getConfig()

        self.logger.info(f"Class [mysql] __init__")

        self.dbconfig = {
            "database": self.config['database']['database'],
            "user": self.config['database']['username'],
            "host": self.config['database']['host'],
            "port": self.config['database']['port'],
            "password": self.config['database']['password']
        }

        if self.config['first_run']:
            self.logger.error("This is the first run of the application please edit the config.json")
            self.config['first_run'] = False
            self.configManager.writeConfig(self.config)
            sys.exit()

        self.pool = mysql.connector.pooling.MySQLConnectionPool(pool_name=self.config['database']['pool_name'],
                                                                pool_size=self.config['database']['pool_size'],
                                                                **self.dbconfig)
        self.logger.info(f"[DATABASE] [mysql] Connection Pool Setup")

    def get_connection(self):
        connection = self.pool.get_connection()
        self.logger.info(f"[DATABASE] [mysql] new PoolConnection: {connection.connection_id}")
        return self.pool.get_connection()
