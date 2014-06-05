__author__ = 'Roderick Lagunas'

from interface.command import CommandInterface
from common import command


class Message(CommandInterface):

    def __init__(self):
        pass

    def main(self, args):
        import module
        command.Core.Help(module, [])

    @staticmethod
    def description():

        return 'ayuda basica'

    @staticmethod
    def usage():

        return command.Core.Color.green + 'help <command>'

    @staticmethod
    def arguments():
        return command.Core.Color.green + 'command' + \
            command.Core.Color.gray + ': un comando en formato ' + \
            command.Core.Color.green + 'commando:accion'

    @staticmethod
    def help():
        return 'permite ver la ayuda detallada de un comando tal como se muestra este.' + "\n" \
               "\t" + 'use el comando ' + \
               command.Core.Color.green + 'list' + \
               command.Core.Color.gray + ' para ver la lista de comandos disponibles'
