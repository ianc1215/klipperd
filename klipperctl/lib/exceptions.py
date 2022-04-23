import os
from klipperctl.lib.constants import Constants
from klipperctl.lib.helpers import info, warn, error


class DaemonInitializationError(Exception):
    """Raised when the system is unable to spawn the klipperd subprocess(es)"""
    __message : str = error("Klipper daemon failed to initialize!")

    def __init__(self):
        super().__init__(self.__message)


class SingleInstanceViolationError(Exception):
    """Raised when a class of method attempts to create a second instance of a singleton class"""
    __message : str = error("Instance of class already exists use get_instance() method!")

    def __init__(self):
        super().__init__(self.__message)


class ConfigurationFileNotFoundError(Exception):
    """Raised when the configuration file cannot be found that the specified system location"""
    __message: str = "The specified file configuration was not found at "
    __path: str = os.path.join(Constants.conf_dir.strip('/') + Constants.conf_file)

    def __init__(self, path: str):
        self.__message = message
        self.__path = path
        super().__init__(self.__message + self.__path)


class ConfigurationLoadError(Exception):
    """Raised when the configuration file cannot be read"""
    pass


class ConfigNotLoadedError(Exception):
    """Raised when a configuration object attempts to be accessed but the configuration has not been loaded yet"""
    __message: str = warn("Configuration has not been loaded!")

    def __init__(self):
        super().__init__(self.__message)


class ConfigurationAlreadyLoadedError(Exception):
    """Raised when the configuration tried to be loaded for a second time, this violates our use of a single
    configuration instance"""
    __message: str = error("Configuration has already been loaded!")

    def __init__(self):
        super().__init__(self.__message)


class ConfigurationChecksumError(Exception):
    """Raised when the configuration checksum does not match the generated checksum, useful for verifing a backup file
    has not been tampered with"""
    pass


class ConfigurationSectionNotFoundError(Exception):
    pass
