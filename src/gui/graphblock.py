# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import os
import sys
import weakref

cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

import ipf.ipfblock.ioport
import geticon
import image_convert


class GraphBlock(QtGui.QGraphicsWidget):
    """ GraphBlock represents IPFBlock in graphics scene
    
    """
    
    block_width = 80
    block_height = 64
    
    # Paint mode constants
    TEXT_PAINT_MODE = 1
    ICON_PAINT_MODE = 2
    IMAGE_PAINT_MODE = 3
    
    def __init__(self, ipf_block_ref, block_name):
        super(GraphBlock, self).__init__()
        self.ipf_block_ref = ipf_block_ref
        self.block_name = block_name
        self.rect_item = BlockPrimitive(self)
        self.rect_item.setRect(0, 0, self.block_width, self.block_height)
        self.setSizePolicy(QtGui.QSizePolicy.Fixed,
                           QtGui.QSizePolicy.Fixed)
        self.resize(self.block_width, self.block_height)
        self.input_ports_items = dict()
        self.output_ports_items = dict()
        for iport in self.ipf_block_ref().input_ports:
            self.input_ports_items[iport] = \
                PortPrimitive(self, self.ipf_block_ref().input_ports[iport])
        for oport in self.ipf_block_ref().output_ports:
            self.output_ports_items[oport] = \
                PortPrimitive(self, self.ipf_block_ref().output_ports[oport])
    
        self.adjust_ports(self.input_ports_items.values(), 0)
        self.adjust_ports(self.output_ports_items.values(), self.block_height)    
        
        self.setAcceptedMouseButtons(QtCore.Qt.LeftButton)
        
        
        
    
    def adjust_ports(self, ports, y_base):
        port_count = len(ports)
        if port_count > 0:
            port_distance = self.block_width / (port_count + 1)
            for i, port_item in enumerate(ports):
                port_item.setRect(0, 
                                  0,
                                  port_item.port_size,
                                  port_item.port_size )
                port_item.setPos((i+1) * port_distance - port_item.port_size / 2, 
                                  y_base - port_item.port_size / 2)

    
    
    
    def set_paint_mode(self, mode):
        """ Sets visualization mode of block
            
            There is 3 paint mode:
            Text - show block type
            Image - show block processing image
            Icon - show block icon
        
        """
        self.rect_item.set_paint_mode(mode)
        
        
    def update_preview_image(self):
        self.rect_item.update_preview_image()
        
        
    def get_preview_image(self):
        return self.rect_item.get_preview_image()
                
                
                

class PortPrimitive(QtGui.QGraphicsEllipseItem):
    
    port_size = 20
    
    def __init__(self, parent, ipf_port):
        super(PortPrimitive, self).__init__(parent)
        self.ipf_port = ipf_port
        brush = self.brush()
        brush.setStyle(QtCore.Qt.SolidPattern)
        brush.setColor(QtCore.Qt.white)
        self.setBrush(brush)
        self.setZValue(10)
        image = geticon.get_image_for_type(ipf_port._data_type.__name__)
        icon_pixmap = QtGui.QPixmap.fromImage(image)
        self.icon = QtGui.QGraphicsPixmapItem(self)
        self.icon.setPixmap(icon_pixmap)
        rect = self.icon.boundingRect()
        icon_x = (self.port_size - rect.width()) / 2
        icon_y = (self.port_size - rect.height()) / 2
        self.icon.setPos(icon_x, icon_y)
         
    
    
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
        # Shift line end from mouse position for prevent overlap of ports  
        grid.set_temp_arrow_end(end.x() - 2 , end.y() + 2)
        grid.highlight_arrow(False)
        port = grid.get_port_at_point(end)
        if port is not None:
            if ipf.ipfblock.ioport.is_connect_allowed(self.ipf_port, port.ipf_port):
                grid.highlight_arrow(True)
        

        
    def mouseReleaseEvent(self, event):
        block = self.parentItem()
        grid = block.parentItem()
        pos = self.mapToScene(event.pos())
        self.setCursor(QtCore.Qt.ArrowCursor)
        grid.disable_temp_arrow()
        dest_port = grid.get_port_at_point(pos)
        if dest_port is not None:
            if ipf.ipfblock.ioport.is_connect_allowed(self.ipf_port, dest_port.ipf_port):
                grid.create_connection(self, dest_port)
            
    
    
class BlockPrimitive(QtGui.QGraphicsRectItem):
    
    def __init__(self, parent):
        super(BlockPrimitive, self).__init__(parent)
        self.selected = False
        self.paint_mode = GraphBlock.TEXT_PAINT_MODE
        self.name_item = QtGui.QGraphicsTextItem(self)
        self.name_item.setTextWidth(GraphBlock.block_width)
        font = self.name_item.font()
        font.setPixelSize(10)
        self.name_item.setFont(font)
        self.name_item.setHtml("<center>%s</center>" % 
                               (self.parentItem().ipf_block_ref().type))
        x = self.name_item.pos().x()
        self.name_item.setPos(x, self.parentItem().block_height / 3)
        
        self.image_item = QtGui.QGraphicsPixmapItem(self)
        x = self.image_item.pos().x()
        y = self.image_item.pos().y()
        self.image_item.setPos(x + self.parentItem().block_width / 4,
                               y + self.parentItem().block_height / 4)
        
        self.preview_pixmap = QtGui.QPixmap()
        
    
    def paint(self, painter, option, widget):
        rect = self.rect()
        brush = painter.brush()
        brush.setStyle(QtCore.Qt.SolidPattern)
        if self.selected:
            brush.setColor(QtGui.QColor(255, 230, 230))
        else:
            brush.setColor(QtCore.Qt.white)
        painter.setBrush(brush)
        painter.drawRoundedRect( rect, 5, 5)
        
        
    def update_preview_image(self):
        ipl_image = self.parentItem().ipf_block_ref().get_preview_image()
        if ipl_image is not None:
            qimage = image_convert.iplimage_to_qimage(ipl_image)
            self.preview_pixmap = QtGui.QPixmap.fromImage(qimage)
            if qimage.isNull():
                self.image_item.setPixmap(QtGui.QPixmap())
            else:
                qpixmap = self.preview_pixmap.scaled(GraphBlock.block_width / 2,
                          GraphBlock.block_height / 2,
                          QtCore.Qt.KeepAspectRatio)
                self.image_item.setPixmap(qpixmap)
    
    
    def get_preview_image(self):
        return self.preview_pixmap
        
        
    def mousePressEvent(self, event):
        self.setCursor(QtCore.Qt.ClosedHandCursor)
        grid = self.parentItem().parentItem()
        grid.block_selected(self)
        
        
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
        block_row, block_column = grid.get_block_cell(block.block_name)
        grid_width, grid_height = grid.get_grid_size()
        if (row != block_row or column != block_column) and \
           row >= 0 and \
           row < grid_height and \
           column >= 0 and \
           column < grid_width:
            grid.move_block(block, row, column)
        self.setCursor(QtCore.Qt.ArrowCursor)


    def set_paint_mode(self, mode):
        if mode == GraphBlock.IMAGE_PAINT_MODE:
            self.paint_mode = mode
            self.name_item.hide()
            self.image_item.show()
        elif mode == GraphBlock.ICON_PAINT_MODE:
            self.paint_mode = mode
            self.name_item.hide()
            self.image_item.show()
        else:
            # Default paint mode is TEXT_PAINT_MODE
            self.paint_mode = GraphBlock.TEXT_PAINT_MODE
            self.name_item.show()
            self.image_item.hide()
        
        
        
        