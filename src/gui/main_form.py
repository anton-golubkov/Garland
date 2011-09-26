# -*- coding: utf-8 -*-


from PySide import QtCore, QtGui
from main_form_ui import Ui_MainWindow
import os
import sys

cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from ipf.ipfgraphloader import get_ipfblock_classes

class MainForm(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._init_blocks_widget()

    
    def _init_blocks_widget(self):
        block_classes = get_ipfblock_classes()
        categories = set()
        for block_class in block_classes.values():
            if len(block_class.category) > 0:
                categories.add(block_class.category)
        
        print categories