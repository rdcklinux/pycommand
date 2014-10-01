#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Roderick Lagunas'

if __name__ == "__main__":
    import os
    import sys

    root_path = os.path.abspath(__file__ + '/../../..')
    sys.path = [root_path] + sys.path
    os.chdir(root_path)

    from app.manager.common import exception, command
    from app.manager import module

    try:
        try:
            command.Core(module, sys.argv)
        except (IndexError, AttributeError), e:
            command.Core(module)
            exit()

        _names = sys.argv[1].split(':')
        _attr = None
        try:
            _attr = getattr(module, _names[0])
        except AttributeError, e:
            print "\n" + 'Modulo %s no disponible.' % sys.argv[1] + ' - ' + e.message + "\n"
            exit()

        _class = getattr(_attr, _names[1].capitalize())

        import re
        regex = re.compile('^\-{1,2}([\w|\d]+)(=(.+))?$')
        args = dict()
        for i, arg in enumerate(sys.argv[2:]):
            result = regex.match(arg)
            if result:
                args[result.group(1)] = args[i] = (result.group(3) if result.group(3) else True)
            else:
                args[i] = arg
        _class().main(args)

    except exception.FinishException:
        print command.Core.Color.sys
