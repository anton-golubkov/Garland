#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Copyright (c) 2011 Anton Golubkov.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Public License v2.0
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# 
# Contributors:
#     Anton Golubkov - initial API and implementation
#-------------------------------------------------------------------------------


from main_form import MainForm
from PySide import QtGui, QtCore
import sys
import os

import graphblock
from ipf.ipfblock.rgb2gray import RGB2Gray
from ipf.ipfblock.imageinput import ImageInput

cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    # Load russian translation
    translator = QtCore.QTranslator()
    translator.load('i18n/ru_RU')
    #app.installTranslator(translator)

    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())
    
