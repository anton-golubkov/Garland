# -*- coding: utf-8 -*-

from PySide import QtGui

class GraphBlock(QtGui.QGraphicsWidget):
    """ GraphBlock represents IPFBlock in graphics scene
    
    """
    
    block_width = 40
    block_height = 32
    port_size = 10
    
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
        for iport in self.block.input_ports:
            self.input_ports_items[iport] = QtGui.QGraphicsEllipseItem(self.rect_item)
        for oport in self.block.output_ports:
            self.output_ports_items[oport] = QtGui.QGraphicsEllipseItem(self.rect_item)
        
        iport_count = len(self.input_ports_items)
        if iport_count > 0:
            iport_distance = self.block_width / (iport_count + 1)
            for i, iport_item in enumerate(self.input_ports_items.values()):
                iport_item.setRect( (i+1) * iport_distance - self.port_size / 2, 
                                   0 - self.port_size / 2,
                                   self.port_size,
                                   self.port_size )
                
        oport_count = len(self.output_ports_items)
        if oport_count > 0:
            oport_distance = self.block_width / (oport_count + 1)
            for i, oport_item in enumerate(self.output_ports_items.values()):
                oport_item.setRect( (i+1) * oport_distance - self.port_size / 2, 
                                   self.block_height - self.port_size / 2,
                                   self.port_size,
                                   self.port_size )
    
    
         
        
    

