# -*- coding: utf-8 -*-

from PySide import QtGui

class GraphBlock(QtGui.QGraphicsWidget):
    """ GraphBlock represents IPFBlock in graphics scene
    
    """
    
    block_width = 40
    block_height = 32
    
    def __init__(self):
        super(GraphBlock, self).__init__()
        self.rect_item = QtGui.QGraphicsRectItem(self)
        self.rect_item.setRect(0, 0, self.block_width, self.block_height)
        self.setSizePolicy(QtGui.QSizePolicy.Fixed,
                           QtGui.QSizePolicy.Fixed)
        self.resize(self.block_width, self.block_height)

