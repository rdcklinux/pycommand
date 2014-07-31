__author__ = 'Roderick Lagunas'
import inspect
import exception


class Core:

    class Color:
        sys = '\033[0;00m'
        darkgray = '\033[0;30m'
        red = '\033[0;31m'
        green = '\033[0;32m'
        brown = '\033[0;33m'
        blue = '\033[0;34m'
        purple = '\033[0;35m'
        cyan = '\033[0;36m'
        gray = '\033[0;37m'

        black = '\033[1;30m'
        yellow = '\033[1;33m'
        white = '\033[1;37m'

        def __init__(self):
            pass

    class List:

        def __init__(self, module, args=None):

            print Core.Color.brown + 'Comandos disponibles:'

            print Core.Color.green + '  help' + "\t" + Core.Color.sys + 'Muestra la ayuda para un comando.'
            print Core.Color.green + '  list' + "\t" + Core.Color.sys + 'Lista los comandos disponibles.'
            for module in inspect.getmembers(module, predicate=inspect.ismodule):
                if module[0] == 'help' or module[0] == 'interface':
                    continue

                print Core.Color.brown + module[0]
                for _class in inspect.getmembers(module[1], predicate=inspect.isclass):
                    if _class[0] == 'CommandInterface':
                        continue
                    
                    if hasattr(_class[1], 'description'):
                        print Core.Color.green + '  ' + module[0] + ':' + _class[0].lower() + \
                            "\t" + Core.Color.sys + str(_class[1].description())

    class Help:

        def __init__(self, module, args):
            if len(args) < 3:
                _class = module.help.Message
            else:
                _names = args[2].split(':')
                _attr = getattr(module, _names[0])
                _class = getattr(_attr, _names[1].capitalize())

            print Core.Color.brown + 'Usage:'
            print "\t" + Core.Color.gray + str(_class.usage())
            print Core.Color.brown + 'Arguments:'
            print "\t" + Core.Color.gray + str(_class.arguments())
            print Core.Color.brown + 'Help:'
            print "\t" + Core.Color.gray + str(_class.help())

    def __init__(self, module, args=None):

        if args:
            _class = getattr(self, args[1].capitalize(), None)
            if _class:
                _class(module, args)
                raise exception.FinishException
        else:
            self.List(module)
