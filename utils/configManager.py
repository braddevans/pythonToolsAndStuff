import json
import os

configFile = "config.json"


class ConfigManager:
    def __init__(self, logger):
        self.logger = logger
        self.logger.debug("Config __init__")

        # todo: implement ssl database connections in future
        self.config = {
            "first_run": True,
            "database": {
                "type": "flatfile"
            }
        }

        if self.checkExists(configFile):
            self.logger.debug(f"Exists [{configFile}]: " + str(self.checkExists(configFile)) + f", Path: {os.getcwd() + os.sep + configFile}")
            self.readConfig()
        else:
            self.writeConfig(self.config)
            self.readConfig()

    def checkExists(self, file):
        return os.path.exists(os.getcwd() + os.sep + file)

    def getConfig(self):
        return self.config

    # ============================= #
    #       json file stuff         #
    # ============================= #

    def readConfig(self):
        with open('config.json') as config_file:
            self.config = json.load(config_file)

    def writeConfig(self, config):
        with open("config.json", "w") as outfile:
            outfile.write(json.dumps(config, indent=2, sort_keys=True))
