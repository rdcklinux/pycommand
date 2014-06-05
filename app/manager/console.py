# -*- coding: utf-8 -*-
__author__ = 'Roderick Lagunas'

import sys
from common import exception, command
import module


if __name__ == "__main__":
    try:
        command.Core(module, sys.argv)
        _names = sys.argv[1].split(':')
        _attr = getattr(module, _names[0])
        _class = getattr(_attr, _names[1].capitalize())

        try:
            _class().main(sys.argv[2:])
        except AttributeError, e:
            print 'Implementacion de %s invalida.' % sys.argv[1] + ' message: ' + str(e)

    except AttributeError, e:
        print 'Modulo %s no disponible.' % sys.argv[1] + ' - ' + e.message

    except IndexError:
        command.Core(module)

    except exception.FinishException:
        print command.Core.Color.sys