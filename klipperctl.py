import os
import sys

from klipperctl.configuration.configparser import Configuration


class Setup(object):
    """
    Since we want to limit access and visibility to argument parser we can initialize it
    inside the class body. This prevents direct manipulation of the ArgumentParser
    """
    from argparse import ArgumentParser

    __instance = None
    __argparser = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        cls.__argparser = cls.ArgumentParser(
            prog="klipperctl",
            description="Control program for initializing printers running Klipper firmware"
        )
        return cls.__instance

    def get_instance(self):
        return self.__instance

    def get_argparser(self):
        return self.__argparser


def main():
    instance = Setup().get_instance()
    args = instance.get_argparser()
    filename = ""

    args.add_argument('-c', '--configuration', dest=filename, help="Specify a custom configuration file to use")
    args.add_argument('-v', '--verbose', action="store_true", help="Enable verbose output to console")

    conf_inst = Configuration()
    conf_inst.load_config()
    conf_inst.get("ender3")

    # End main


if __name__ == '__main__':
    main()
