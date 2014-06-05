__author__ = 'Roderick Lagunas'

from interface.command import CommandInterface
from common import command


class Hello(CommandInterface):

    name = 'nadie'

    def __init__(self):
        pass

    def main(self, args):
        if len(args):
            self.name = args[0]

        print 'Test de hola mundo para ' + self.name

    @staticmethod
    def description():

        return "Descripcion para test hello"

    @staticmethod
    def usage():

        return command.Core.Color.green + 'test:hello [name]'

    @staticmethod
    def arguments():
        return command.Core.Color.green + 'name' + \
            command.Core.Color.gray + ': a String'

    @staticmethod
    def help():
        return "ayuda detallada para test hello"





