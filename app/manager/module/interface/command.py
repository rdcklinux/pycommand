__author__ = 'Roderick Lagunas'

from abc import ABCMeta, abstractmethod


class CommandInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def main(self, args):
        pass

    @staticmethod
    @abstractmethod
    def description():
        pass

    @staticmethod
    @abstractmethod
    def usage():
        pass

    @staticmethod
    @abstractmethod
    def arguments():
        pass

    @staticmethod
    @abstractmethod
    def help():
        pass