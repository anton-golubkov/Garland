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
        self.block_classes = get_ipfblock_classes()
        categories = set()
        for block in self.block_classes.values():
                categories.add(block.category)
        category_items = dict()
        for category in categories:
            category_items[category] = QtGui.QTreeWidgetItem(None)
            category_items[category].setText(0, category)
        for block in self.block_classes.values():
            block_item = QtGui.QTreeWidgetItem(category_items[block.category])
            block_item.setText(0, block.type)
        
        self.ui.blocks_tree.insertTopLevelItems(0, category_items.values())


  