from os.path import exists, join
from sys import platform

import toml
from colors import color
from klipperctl.lib.constants import Constants
from klipperctl.lib.helpers import warn, error
from klipperctl.lib.exceptions import ConfigurationFileNotFoundError, ConfigNotLoadedError, \
    ConfigurationAlreadyLoadedError, ConfigurationSectionNotFoundError


class Configuration:

    __instance = None
    __config_parser = None
    __config_writer = None
    __config_data = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        cls.__config_parser = toml.decoder
        cls.__config_writer = toml.encoder

        return cls.__instance

    def load_config(self, config_dir=Constants.conf_dir, config_file=Constants.conf_file):

        __config_path = None

        # Strip the trailing slash off the configuration directory
        if platform == "win32":
            config_dir.strip('\\')
            __config_path = join(config_dir + "\\" + config_file)
        elif platform == "linux" or "darwin":
            config_dir.strip('/')
            __config_path = join(config_dir + '/' + config_file)

        # Only load the configuration once, always refer to the same copy of the configuration for all lookups
        if self.__config_data is None:

            try:
                """
                Only try to read the config if it exists since trying to read a file that doesn't exist would result
                in an error anyway
                """
                if exists(__config_path):
                    print("Loaded configuration " + str(__config_path))
                    self.__config_data = self.__config_parser.load(__config_path)

            except ConfigurationFileNotFoundError:

                raise ConfigurationFileNotFoundError(str(__config_path))

                # Throw an exception that configuration has been loaded
        elif self.__config_data is not None:

            raise ConfigurationAlreadyLoadedError()

    """
    Returns the configuration file section
    """
    def get(self, section: str):

        if self.__exists(section):
            return self.__config_data[section]

    """
    Searches the configuration file for the specified sections. If the section exists the method returns True
    """
    def search(self, section: str):
        return self.__exists(section)

    """
    Validate a configuration section is reachable
    """
    def __exists(self, section: str):
        if section in self.__config_data:
            return True
        else:
            raise ConfigurationSectionNotFoundError()
            # return False
