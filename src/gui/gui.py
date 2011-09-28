#!/usr/bin/python
# -*- coding: utf-8 -*-

from main_form import MainForm
from PySide import QtGui, QtCore
import sys
import os

import graphblock

cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    # Load russian translation
    translator = QtCore.QTranslator()
    translator.load('i18n/ru_RU')
    app.installTranslator(translator)

    main_form = MainForm()
    main_form.show()
    block1 = graphblock.GraphBlock()
    main_form.scheme.add_block(block1, 0, 0)
    block2 = graphblock.GraphBlock()
    main_form.scheme.add_block(block2, 1, 1)
    block3 = graphblock.GraphBlock()
    main_form.scheme.add_block(block3, 2, 2)
    block4 = graphblock.GraphBlock()
    main_form.scheme.add_block(block4, 3, 3)
    sys.exit(app.exec_())
    
