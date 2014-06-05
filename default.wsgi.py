# -*- coding: utf-8 -*-


import sys
import os

root_path = os.path.dirname(__file__)
sys.path = [root_path] + sys.path
os.chdir(root_path)

from app.manager.rest import app as application

application.debug = True
