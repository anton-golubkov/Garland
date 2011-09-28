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
    
        self.adjust_ports(self.input_ports_items.values(), 0)
        self.adjust_ports(self.output_ports_items.values(), self.block_height)    
        
    
    def adjust_ports(self, ports, y_base):
        port_count = len(ports)
        if port_count > 0:
            port_distance = self.block_width / (port_count + 1)
            for i, port_item in enumerate(ports):
                port_item.setRect( (i+1) * port_distance - self.port_size / 2, 
                                   y_base - self.port_size / 2,
                                   self.port_size,
                                   self.port_size )
    
         
        
    

