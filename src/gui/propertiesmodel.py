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
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import os
import sys
import weakref


cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class PropertiesModel(QtCore.QAbstractTableModel):
    """ Subclass of QAbstractTableModel for handle IPFBlock properties data
    
    """
    
    def __init__(self, ipf_block_ref=None):
        super(PropertiesModel, self).__init__()
        
        if ipf_block_ref is not None:
            self.ipf_block_ref = ipf_block_ref
        else:
            self.ipf_block_ref = None
        
        
    def rowCount(self, index=None):
        if self.ipf_block_ref is None or \
           self.ipf_block_ref() is None :
            return 0
        else:
            return len(self.ipf_block_ref().properties)
    
    
    def columnCount(self, index=None):
        return 2
    
    
    def data(self, index, role):
        if not index.isValid():
            return None
        
        if role != QtCore.Qt.DisplayRole and role != QtCore.Qt.EditRole:
            return None
        
        if index.row() >= self.rowCount(index) or \
           index.column() >= self.columnCount(index):
            return None
        
        if self.ipf_block_ref is None:
            return None
        
        if self.ipf_block_ref() is None:
            return None
        
        key = self.ipf_block_ref().properties.keys()[index.row()]
        value = self.ipf_block_ref().properties[key].get_value_representation()
        
        if index.column() == 0:
            return key
        elif index.column() == 1:
            return value
        else:
            return None 
      
        
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if self.ipf_block_ref is None or \
           self.ipf_block_ref() is None:
            return False
        if index.isValid() and \
           role == QtCore.Qt.EditRole and \
           index.column() == 1:
            key = self.ipf_block_ref().properties.keys()[index.row()]
            self.ipf_block_ref().properties[key].set_value(value)
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
        
    
    def get_property(self, row):
        """ PropertiesModel specific function
        
            Returns property for given row
        """
        
        if row >= self.rowCount():
            return None
        
        if self.ipf_block_ref is None or \
           self.ipf_block_ref() is None:
            return False
        
        key = self.ipf_block_ref().properties.keys()[row]
        return self.ipf_block_ref().properties[key]
        


        
