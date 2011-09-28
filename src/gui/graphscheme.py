# -*- coding: utf-8 -*-


from PySide import QtGui, QtCore

class GraphScheme( QtGui.QGraphicsScene):
    """ Graph scheme drawing class
    
        This class inherits from QtGui.QGraphicsScene and add functions
        for manage GraphBlocks objects in scheme.
    
    """
    
    def __init__(self ):
        super(GraphScheme, self).__init__()
        self.layout = QtGui.QGraphicsGridLayout()
        self.form = QtGui.QGraphicsWidget()
        self.form.setLayout(self.layout)
        self.addItem(self.form)
        self.form.setPos(0, 0)
        gradient = QtGui.QLinearGradient(0, 0, 0, 4000)
        gradient.setColorAt( 0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt( 1, QtGui.QColor(0, 0, 255))
        self.setBackgroundBrush(gradient)
     
    
    def add_block(self, block, row, column):
        """ Add GraphBlock to scheme into specified row and column
        
        """   
        self.layout.addItem(block, row, column)
    
    
    
    