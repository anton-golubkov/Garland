#!/usr/bin/python
# -*- coding: utf-8 -*-


from PySide import QtCore, QtGui
from main_form_ui import Ui_MainWindow


class MainForm(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

