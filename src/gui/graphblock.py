# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore

import ipf.ioport

class GraphBlock(QtGui.QGraphicsWidget):
    """ GraphBlock represents IPFBlock in graphics scene
    
    """
    
    block_width = 80
    block_height = 64
    port_size = 20
    
    def __init__(self, block, name):
        super(GraphBlock, self).__init__()
        self.block = block
        self.name = name
        self.rect_item = BlockPrimitive(self)
        self.rect_item.setRect(0, 0, self.block_width, self.block_height)
        self.setSizePolicy(QtGui.QSizePolicy.Fixed,
                           QtGui.QSizePolicy.Fixed)
        self.resize(self.block_width, self.block_height)
        self.name_item = QtGui.QGraphicsTextItem(self.rect_item)
        self.name_item.setTextWidth(self.block_width)
        font = self.name_item.font()
        font.setPixelSize(10)
        self.name_item.setFont(font)
        self.name_item.setHtml("<center>%s</center>" % (self.name))
        self.input_ports_items = dict()
        self.output_ports_items = dict()
        for iport in self.block.input_ports:
            self.input_ports_items[iport] = \
                PortPrimitive(self, self.block.input_ports[iport])
        for oport in self.block.output_ports:
            self.output_ports_items[oport] = \
                PortPrimitive(self, self.block.output_ports[oport])
    
        self.adjust_ports(self.input_ports_items.values(), 0)
        self.adjust_ports(self.output_ports_items.values(), self.block_height)    
        
        self.setAcceptedMouseButtons(QtCore.Qt.LeftButton)
        
    
    def adjust_ports(self, ports, y_base):
        port_count = len(ports)
        if port_count > 0:
            port_distance = self.block_width / (port_count + 1)
            for i, port_item in enumerate(ports):
                port_item.setRect( (i+1) * port_distance - self.port_size / 2, 
                                   y_base - self.port_size / 2,
                                   self.port_size,
                                   self.port_size )
                
        
    
        
    

class PortPrimitive(QtGui.QGraphicsEllipseItem):
    def __init__(self, parent, ipf_port):
        super(PortPrimitive, self).__init__(parent)
        self.ipf_port = ipf_port
        brush = self.brush()
        brush.setStyle(QtCore.Qt.SolidPattern)
        brush.setColor(QtCore.Qt.white)
        self.setBrush(brush)
        self.setZValue(10)
    
    
    def get_port_center(self):
        r = self.rect()
        center = QtCore.QPoint(r.x() + r.width()/2, r.y() + r.height()/2)
        center = self.mapToScene(center)
        return center
    
    
    def mousePressEvent(self, event):
        self.setCursor(QtCore.Qt.CrossCursor)
        grid = self.parentItem().parentItem()
        grid.enable_temp_arrow()
        center = self.get_port_center()
        grid.set_temp_arrow_begin(center.x(), center.y())
    
        
    def mouseMoveEvent(self, event):
        if QtCore.QLineF(event.screenPos(), \
                         event.buttonDownScreenPos(QtCore.Qt.LeftButton)).length() < \
                         QtGui.QApplication.startDragDistance():
            return
        
        grid = self.parentItem().parentItem()
        beg = self.mapToScene(event.buttonDownPos(QtCore.Qt.LeftButton))
        end = self.mapToScene(event.pos())
        grid.set_temp_arrow_end(end.x(), end.y())
        port = grid.get_port_at_point(end)
        

        
    def mouseReleaseEvent(self, event):
        block = self.parentItem()
        grid = block.parentItem()
        pos = self.mapToScene(event.pos())
        self.setCursor(QtCore.Qt.ArrowCursor)
        grid.disable_temp_arrow()
            
    
    
class BlockPrimitive(QtGui.QGraphicsRectItem):
    
    def __init__(self, parent):
        super(BlockPrimitive, self).__init__(parent)

        
    
    def paint(self, painter, option, widget):
        rect = self.rect()
        brush = painter.brush()
        brush.setStyle(QtCore.Qt.SolidPattern)
        brush.setColor(QtCore.Qt.white)
        painter.setBrush(brush)
        painter.drawRoundedRect( rect, 5, 5)
        
        
    def mousePressEvent(self, event):
        self.setCursor(QtCore.Qt.ClosedHandCursor)
        
        
    def mouseMoveEvent(self, event):
        if QtCore.QLineF(event.screenPos(), \
                         event.buttonDownScreenPos(QtCore.Qt.LeftButton)).length() < \
                         QtGui.QApplication.startDragDistance():
            return
        
        grid = self.parentItem().parentItem()
        grid.enable_dummy_block()
        pos = self.mapToScene(event.pos())
        row, column = grid.get_cell_in_point( (pos.x(), pos.y()) )
        grid.set_dummy_block_cell(row, column)
        
        
    def mouseReleaseEvent(self, event):
        block = self.parentItem()
        grid = block.parentItem()
        grid.disable_dummy_block()
        pos = self.mapToScene(event.pos())
        row, column = grid.get_cell_in_point( (pos.x(), pos.y()) )
        block_row, block_column = grid.get_block_cell(block)
        grid_width, grid_height = grid.get_grid_size()
        if (row != block_row or column != block_column) and \
           row < grid_height and \
           column < grid_width:
            grid.move_block(block, row, column)
        self.setCursor(QtCore.Qt.ArrowCursor)
        