# -*- coding: utf-8 -*-

from PySide import QtGui

class GraphBlock(QtGui.QGraphicsWidget):
    """ GraphBlock represents IPFBlock in graphics scene
    
    """
    
    block_width = 40
    block_height = 32
    
    def __init__(self, block):
        super(GraphBlock, self).__init__()
        self.block = block
        self.rect_item = QtGui.QGraphicsRectItem(self)
        self.rect_item.setRect(0, 0, self.block_width, self.block_height)
        self.setSizePolicy(QtGui.QSizePolicy.Fixed,
                           QtGui.QSizePolicy.Fixed)
        self.resize(self.block_width, self.block_height)
        self.name_item = QtGui.QGraphicsTextItem(self.rect_item)
        self.name_item.setTextWidth(self.block_width)
        font = self.name_item.font()
        font.setPixelSize(5)
        self.name_item.setFont(font)
        self.name_item.setHtml("<center>%s</center>" % (self.block.type))
        self.input_ports_items = dict()
        self.output_ports_items = dict()
        
    

