# -*- coding: utf-8 -*-


from PySide import QtCore, QtGui

import os
import sys
import cv

cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

from ipf.ipftype.ipfinttype import IPFIntType
from ipf.ipftype.ipfimage1ctype import IPFImage1cType
from ipf.ipftype.ipfimage3ctype import IPFImage3cType
from ipf.ipftype.ipffloattype import IPFFloatType
from ipf.ipftype.ipfrgbtype import IPFRGBType
from ipf.ipftype.ipfstringtype import IPFStringType
from ipf.ipftype.ipfdicttype import IPFDictType
from ipf.ipfblock.property import Property


class PropertyEditorDelegate(QtGui.QItemDelegate):
    """ Property edit delegate class
    
        Create editor widget with response to Property data type
    """
    
    def __init__(self, parent=None):
        super(PropertyEditorDelegate, self).__init__(parent)
    
    
    def createEditor(self, parent, option, index):
        """ Create QWidget for edit property
        
            Type of QWidget determined by property data type
        """
        
        row = index.row()
        property = index.model().get_property(row)
        if property is None:
            return None
        
        data_type = property.get_data_type()
        
        editor = None

        if data_type == IPFIntType:
            editor = self.create_int_editor(parent, property)
        elif data_type == IPFFloatType:
            editor = self.create_float_editor(parent, property)
        elif data_type == IPFRGBType:
            editor = self.create_rgb_editor(parent, property)
        elif data_type == IPFStringType:
            editor = self.create_string_editor(parent, property)
        elif issubclass(data_type, IPFDictType):
            editor = self.create_dict_editor(parent, property)

        return editor;
    
    
    def setEditorData(self, editor, index):
        row = index.row()
        property = index.model().get_property(row)
        value_repr = property.get_value_representation()
        data_type = property.get_data_type()
        if data_type == IPFIntType:
            # QSpinBox widget
            editor.setValue(int(value_repr))
        elif data_type == IPFFloatType:
            # QDoubleSpinBox widget
            editor.setValue(float(value_repr))
        elif data_type == IPFRGBType:
            # Not implemented
            pass
        elif data_type == IPFStringType:
            # QLineEdit widget
            editor.setText(value_repr)
        elif issubclass(data_type, IPFDictType):
            # QComboBox widget
            item_index = editor.findText(value_repr)
            editor.setCurrentIndex(item_index)
            
            
    def setModelData(self, editor, model, index):
        row = index.row()
        property = index.model().get_property(row)
        data_type = property.get_data_type()
        value = None
        if data_type == IPFIntType:
            # QSpinBox widget
            value = editor.value()
        elif data_type == IPFFloatType:
            # QDoubleSpinBox widget
            value = editor.value()
        elif data_type == IPFRGBType:
            # Not implemented
            pass
        elif data_type == IPFStringType:
            # QLineEdit widget
            value = editor.text()
        elif issubclass(data_type, IPFDictType):
            # QComboBox widget
            value =  editor.currentText()
        
        property.set_value(value)
        index.model().dataChanged.emit(index, index)
    
    
    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
    
        
    def create_int_editor(self, parent, property):
        editor = QtGui.QSpinBox(parent)
        if property.min_value is not None:
            editor.setMinimum(property.min_value)
        if property.max_value is not None:
            editor.setMaximum(property.max_value)
        return editor
    
    
    def create_float_editor(self, parent, property):
        editor = QtGui.QDoubleSpinBox(parent)
        editor.setDecimals(1)
        if property.min_value is not None:
            editor.setMinimum(property.min_value)
        if property.max_value is not None:
            editor.setMaximum(property.max_value)
        return editor
    
    
    def create_rgb_editor(self, parent, property):
        # Not implemented yet
        return None
    
    
    def create_string_editor(self, parent, property):
        editor = QtGui.QLineEdit(parent)
        return editor
    
    
    def create_dict_editor(self, parent, property):
        editor = QtGui.QComboBox(parent)
        for i, value in enumerate(property._data_type.get_value_list()):
            value_repr = property.get_data_type().get_value_representation(value)
            editor.insertItem(i, value_repr)
            
        return editor
    
    
    
    
    