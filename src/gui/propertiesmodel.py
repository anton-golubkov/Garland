# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import os
import sys


cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)



class PropertiesModel(QtCore.QAbstractTableModel):
    """ Subclass of QAbstractTableModel for handle IPFBlock properties data
    
    """
    
    def __init__(self, block):
        super(PropertiesModel, self).__init__()
        self.block = block
        
        
    def rowCount(self, index):
        return len(self.block.properties)
    
    
    def columnCount(self, index):
        return 2
    
    
    def data(self, index, role):
        if not index.isValid():
            return None
        
        if role != QtCore.Qt.DisplayRole and role != QtCore.Qt.EditRole:
            return None
        
        if index.row() >= self.rowCount(index) or \
           index.column() >= self.columnCount(index):
            return None
        
        key = self.block.properties.keys()[index.row()]
        value = self.block.properties[key].value
        
        if index.column() == 0:
            return key
        elif index.column() == 1:
            return value
        else:
            return None 
      
        
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid() and \
           role == QtCore.Qt.EditRole and \
           index.column() == 1:
            key = self.block.properties.keys()[index.row()]
            self.block.properties[key].set_value(value)
            self.dataChanged.emit(index, index)
            return True
        else:
            return False
    
        
    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return None
        
        if orientation == QtCore.Qt.Horizontal:
            if section == 0:
                return "Property"
            else:
                return "Value"
        else:
            return None 
    
    
    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled
        
        if index.column() == 1:
            return super(PropertiesModel, self).flags(index) | \
                   QtCore.Qt.ItemIsEditable
        else:
            return super(PropertiesModel, self).flags(index)
        
        