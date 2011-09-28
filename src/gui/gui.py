#!/usr/bin/python
# -*- coding: utf-8 -*-

from main_form import MainForm
from PySide import QtGui, QtCore
import sys
import os


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
    sys.exit(app.exec_())
    
