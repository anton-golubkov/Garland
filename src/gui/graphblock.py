# -*- coding: utf-8 -*-

from PySide import QtGui

class GraphBlock(QtGui.QGraphicsWidget):
    """ GraphBlock represents IPFBlock in graphics scene
    
    """
    
    def __init__(self):
        super(GraphBlock, self).__init__()
        self.rect_item = QtGui.QGraphicsRectItem(self)
        self.rect_item.setRect(0, 0, 10, 10)

