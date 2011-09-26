#!/usr/bin/python
# -*- coding: utf-8 -*-

from main_form import MainForm
from PySide import QtGui, QtCore
import sys

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())
    
