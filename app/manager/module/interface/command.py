__author__ = 'Roderick Lagunas'


class CommandInterface:

    def __init__(self):
        pass

    def main(self, args):
        raise NotImplementedError

    @staticmethod
    def description():
        raise NotImplementedError

    @staticmethod
    def usage():
        raise NotImplementedError

    @staticmethod
    def arguments():
        raise NotImplementedError

    @staticmethod
    def help():
        raise NotImplementedError