# -*- coding: utf-8 -*-


from PySide import QtGui, QtCore

from ipf.ipfgraph import IPFGraph
from ipf.ipfblock.ioport import IPort, OPort
import graphblock
from graphblock import GraphBlock

class GraphScheme( QtGui.QGraphicsScene):
    """ Graph scheme drawing class
    
        This class inherits from QtGui.QGraphicsScene and add functions
        for manage GraphBlocks objects in scheme.
    
    """
    
    def __init__(self, parent=None):
        super(GraphScheme, self).__init__(parent)
        gradient = QtGui.QLinearGradient(0, 0, 0, 4000)
        gradient.setColorAt( 0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt( 1, QtGui.QColor(0, 0, 255))
        self.setBackgroundBrush(gradient)
        self.ipf_graph = IPFGraph()
        self._grid = GraphGrid(self.ipf_graph)
        self.addItem(self._grid)
        self._grid.adjust_grid_size()
        
        # Counter for block names
        self.block_number = 0
    
    def add_block(self, block, row, column):
        self.block_number += 1
        self.ipf_graph.add_block(block.ipf_block.type + str(self.block_number),
                                 block.ipf_block, 
                                 row, 
                                 column)
        self._grid.add_block(block, row, column)
        
        
    def delete_selected(self):
        self._grid.delete_selected()
        
        
    def get_selected_block(self):
        return self._grid.get_selected_block()


class GraphGrid(QtGui.QGraphicsRectItem):
    """ Graphics grid class, used in GraphScheme
    
    """
    
    cell_width = 100
    cell_height = 120
    left_margin = 40
    top_margin = 40
    
    
    def __init__(self, ipf_graph, parent=None):
        super(GraphGrid, self).__init__(parent)
        self.ipf_graph = ipf_graph
        self.adjust_grid_size()
        
        # Set of GraphBlock objects
        self.graph_blocks = set()
        
        # Dummy block used to show dragged block position
        self.dummy_block = QtGui.QGraphicsRectItem(self)
        self.dummy_block.setRect(0, 0, self.cell_width, self.cell_height)
        self.dummy_block.hide()
        
        # Temporary connection arrow
        self.temp_arrow = QtGui.QGraphicsLineItem(self)
        self.temp_arrow.hide() 
        self.temp_arrow.setZValue(20)
        
        # Connection lines
        self.connection_arrows = []
        
        # Current selected block
        self.selected_block = None
        
        
    def paint(self, painter, option, widget):
        pen = painter.pen()
        pen.setColor( QtGui.QColor(200, 200, 200) )
        pen.setWidth(1)
        painter.setPen(pen)
        
        grid_width, grid_height = self.ipf_graph.get_grid_size()
        width = self.cell_width * grid_width + 2 * self.left_margin
        height = self.cell_height * grid_height + 2 * self.top_margin
        for x in range(self.left_margin, width, self.cell_width):
            painter.drawLine(x, 0, x, height)
        for y in range(self.top_margin, height, self.cell_height):
            painter.drawLine(0, y, width, y)
        
    
    def get_cell_in_point(self, point):
        column = int((point[0] - self.left_margin) / self.cell_width)
        row = int((point[1] - self.top_margin) / self.cell_height)
        return (row, column)
    
    
    def adjust_grid_size(self):
        grid_width, grid_height = self.ipf_graph.get_grid_size()
        self.setRect(0, 
                     0, 
                     grid_width * self.cell_width + 2 * self.left_margin,
                     grid_height * self.cell_height + 2 * self.top_margin)
        
    
    def add_block(self, block, row, column):
        """ Add GraphBlock to scheme into specified row and column
        
        """   
        block.setParentItem(self)
        self.graph_blocks.add(block)
        self.update_block_positions()
            
    
    def move_block(self, block, row, column):
        from_cell = self.ipf_graph.get_block_cell(block.ipf_block)
        if from_cell is not None and self.ipf_graph.grid_cell_empty(row, column):
            self.ipf_graph.move_block(block.ipf_block, row, column)
            self.update_block_positions()
            self.disable_dummy_block()
            # Enlarge grid if block moved to last row / column
            grid_width, grid_height = self.ipf_graph.get_grid_size()
            if (row == grid_height - 1) and grid_height < self.ipf_graph.max_grid_height:
                self.ipf_graph.add_row()
            if (column == grid_width - 1) and grid_width < self.ipf_graph.max_grid_width:
                self.ipf_graph.add_column()
            self.adjust_grid_size() 
            self.update_connection_arrows()
    
    
    def remove_block(self, block):
        block_name = self.ipf_graph.get_block_name(block.ipf_block)
        block.setParentItem(None)
        self.scene().removeItem(block)
        self.ipf_graph.remove_block(block_name)
        self.graph_blocks.remove(block)
        self.update_connection_arrows()
    
    
    def update_block_positions(self):
        for graph_block in self.graph_blocks:
            row, column = self.ipf_graph.get_block_cell(graph_block.ipf_block)
            x, y = self.get_block_position(row, \
                                           column, \
                                           GraphBlock.block_width, \
                                           GraphBlock.block_width)
            graph_block.setPos(x, y)
                    
    
    def get_block_position(self, row, column, block_width, block_height):
        x = self.cell_width * column + self.left_margin
        y = self.cell_height * row + self.top_margin
        shift_x = (self.cell_width - block_width) / 2
        shift_y = (self.cell_height - block_height) / 2
        x += shift_x
        y += shift_y
        return (x, y)
            
        
    def enable_dummy_block(self):
        self.dummy_block.show()
        
        
    def disable_dummy_block(self):
        self.dummy_block.hide()
        
        
    def set_dummy_block_cell(self, row, column):
        grid_width, grid_height = self.ipf_graph.get_grid_size()
        if row < 0 or \
           row >= grid_height or \
           column < 0 or\
           column >= grid_width:
            # Don`t allow move block outside grid
            return
        rect = self.dummy_block.rect()
        width = rect.width()
        height = rect.height()
        x, y = self.get_block_position(row, column, width, height)
        self.dummy_block.setPos(x, y)
        pen = self.dummy_block.pen()
        if not self.ipf_graph.grid_cell_empty(row, column):
            pen.setColor( QtCore.Qt.red)
        else:
            pen.setColor( QtCore.Qt.black)
        self.dummy_block.setPen(pen)
    
        
    def enable_temp_arrow(self):
        self.temp_arrow.show()
        
        
    def disable_temp_arrow(self):
        self.temp_arrow.hide()
        
        
    def set_temp_arrow_begin(self, x, y):
        self.temp_arrow.setLine(x, y, x, y)
        
        
    def set_temp_arrow_end(self, x, y):
        line = self.temp_arrow.line()
        line.setP2( QtCore.QPoint(x, y) )
        self.temp_arrow.setLine(line)
        
        
    def highlight_arrow(self, highlight):
        pen = self.temp_arrow.pen()
        if highlight:
            pen.setColor(QtCore.Qt.green)
        else:
            pen.setColor(QtCore.Qt.black)
        self.temp_arrow.setPen(pen)
    
        
    def get_port_at_point(self, pos):
        items = self.scene().items(pos)
        for item in items:
            if item is not None:
                if type(item) == graphblock.PortPrimitive:
                    return item
    
    def create_connection(self, port1, port2):
        scheme = self.scene()
        ipf_graph = scheme.ipf_graph
        iport_prim = None
        oport_prim = None
        if type(port1.ipf_port) == IPort:
            iport_prim = port1
            oport_prim = port2
        else:
            iport_prim = port2
            oport_prim = port1
        
        ipf_graph.add_connection(oport_prim.ipf_port, iport_prim.ipf_port)
        self.update_connection_arrows()
        
        # Notify main_form about graph changing
        main_form = self.scene().parent()
        main_form.graph_changed()
        
        
    def update_connection_arrows(self):
        """ Recreate all connection lines in GraphScheme
        
        """
        
        for arrow in self.connection_arrows:
            arrow.setParentItem(None)
            self.scene().removeItem(arrow)
        self.connection_arrows = []
        

        grid_width, grid_height = self.ipf_graph.get_grid_size()
        
        for connection in self.ipf_graph.connections:
            iport = connection._iport
            oport = connection._oport
            iblock = iport._owner_block
            oblock = oport._owner_block
            iport_name = iblock.get_port_name(iport)
            oport_name = oblock.get_port_name(oport)
            iblock_prim = self.get_block_primitive_from_block(iblock)
            oblock_prim = self.get_block_primitive_from_block(oblock)
            if iblock_prim is None or oblock_prim is None:
                raise ValueError("IPFBlock not found in scheme")
            
            # Find port primitives
            iport_prim = iblock_prim.input_ports_items[iport_name]
            oport_prim = oblock_prim.output_ports_items[oport_name]
            arrow = self.create_connection_arrow(oport_prim, iport_prim)
            self.connection_arrows.append(arrow)
       
            
    def create_connection_arrow(self, oport_prim, iport_prim):
        begin = oport_prim.get_port_center()
        end = iport_prim.get_port_center()
        row = int( (begin.y() - self.top_margin) / self.cell_height) + 1
        grid_line_y = self.top_margin + row * self.cell_height
        
        arrow = QtGui.QGraphicsPathItem(self)
        path = QtGui.QPainterPath()
        path.moveTo(begin.x(), begin.y())
        path.lineTo(begin.x(), grid_line_y)
        path.lineTo(end.x(), grid_line_y)
        path.lineTo(end.x(), end.y())  
        arrow.setPath(path)
        pen = arrow.pen()
        pen.setWidth(4)
        pen.setColor( QtGui.QColor(113, 153, 213))
        pen.setJoinStyle(QtCore.Qt.RoundJoin)
        pen.setCapStyle(QtCore.Qt.RoundCap)
        arrow.setPen(pen)

        return arrow
    
    
    def block_selected(self, block_primitive):
        """ Notification of block selection change
        
        """
        if self.selected_block is not None:
            self.selected_block.selected = False
            self.selected_block.update()
            
        self.selected_block = block_primitive
        self.selected_block.selected = True
        self.selected_block.update()
        
        ipf_block = block_primitive.parentItem().ipf_block
        main_form = self.scene().parent()
        main_form.block_selected(ipf_block)
        
        
    def get_block_primitive_from_block(self, block):
        for graph_block in self.graph_blocks:
            if block == graph_block.ipf_block:
                return graph_block
        return None
    
    
    def get_block_cell(self, ipf_block):
        return self.ipf_graph.get_block_cell(ipf_block)
    
    
    def get_grid_size(self):
        return self.ipf_graph.get_grid_size()
            
        
    def delete_selected(self):
        if self.selected_block is not None:
            self.remove_block(self.selected_block.parentItem())
            del self.selected_block
            self.selected_block = None
    
    
    def get_selected_block(self):
        return self.selected_block.parentItem().ipf_block
            
    