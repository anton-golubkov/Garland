# -*- coding: utf-8 -*-

from PySide import QtGui

class GraphBlock(QtGui.QGraphicsWidget):
    """ GraphBlock represents IPFBlock in graphics scene
    
    """
    
    def __init__(self, parent=None, wFlags=0):
        super(GraphBlock, self).__init__(parent, wFlags)

