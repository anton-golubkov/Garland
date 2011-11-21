# -*- coding: utf-8 -*-


from PySide import QtGui, QtCore
import weakref

from ipf.ipfgraph import IPFGraph
from ipf.ipfblock.ioport import IPort, OPort
import graphblock
from graphblock import GraphBlock

class GraphScheme( QtGui.QGraphicsScene):
    """ Graph scheme drawing class
    
        This class inherits from QtGui.QGraphicsScene and add functions
        for manage GraphBlocks objects in scheme.
    
    """
    
    def __init__(self, parent=None, ipf_graph=None):
        super(GraphScheme, self).__init__(parent)
        gradient = QtGui.QLinearGradient(0, 0, 0, 4000)
        gradient.setColorAt( 0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt( 1, QtGui.QColor(0, 0, 255))
        self.setBackgroundBrush(gradient)
        self._grid = GraphGrid(ipf_graph)
        self.addItem(self._grid)
        self._grid.adjust_grid_size()
        
    
    def add_block(self, block_type, row, column):
        ipf_block_ref = self._grid.ipf_graph.add_block(block_type,
                                             None, 
                                             row, 
                                             column)
        block_name = self._grid.ipf_graph.get_block_name(ipf_block_ref())
        block = graphblock.GraphBlock(ipf_block_ref, block_name)
        self._grid.add_block(block, row, column)
        
        
    def delete_selected(self):
        self._grid.delete_selected()
        
        
    def get_selected_block(self):
        return self._grid.get_selected_block()
    
    
    def load_graph(self, ipf_graph):
        self._grid.load_graph(ipf_graph)
        
        
    def process(self):
        return self._grid.ipf_graph.process()
    
    
    def save_graph(self, file_name):
        self._grid.ipf_graph.save(file_name)
        
        
    def set_block_paint_mode(self, mode):
        self._grid.set_block_paint_mode(mode)


    def update(self):
        self._grid.update()





class GraphGrid(QtGui.QGraphicsRectItem):
    """ Graphics grid class, used in GraphScheme
    
    """
    
    cell_width = 100
    cell_height = 120
    left_margin = 40
    top_margin = 40
    
    
    # Inner class for represent connection arrow between blocks     
    class ConnectionArrow(QtGui.QGraphicsPathItem):
    
        NORMAL_COLOR = QtGui.QColor(113, 153, 213)
        SELECTED_COLOR = QtGui.QColor(240, 30, 20)
        
        
        def __init__(self, parent, begin, end):
            super(GraphGrid.ConnectionArrow, self).__init__(parent)
            row = int( (begin.y() - GraphGrid.top_margin) / GraphGrid.cell_height) + 1
            grid_line_y = GraphGrid.top_margin + row * GraphGrid.cell_height
            
            path = QtGui.QPainterPath()
            path.moveTo(begin.x(), begin.y())
            path.lineTo(begin.x(), grid_line_y)
            path.lineTo(end.x(), grid_line_y)
            path.lineTo(end.x(), end.y())  
            self.setPath(path)
            pen = self.pen()
            pen.setWidth(4)
            pen.setColor( self.NORMAL_COLOR)
            pen.setJoinStyle(QtCore.Qt.RoundJoin)
            pen.setCapStyle(QtCore.Qt.RoundCap)
            self.setPen(pen)
            self.selected = False
            self.setZValue(-1)
            
            
        def mousePressEvent(self, event):
            grid = self.parentItem()
            grid.connection_arrow_selected(self)
            
            
        def update(self):
            pen = self.pen()
            if self.selected:
                pen.setColor(self.SELECTED_COLOR)
            else:
                pen.setColor(self.NORMAL_COLOR)
            self.setPen(pen)   

    
    
    def __init__(self, ipf_graph, parent=None):
        super(GraphGrid, self).__init__(parent)
        if ipf_graph is None:
            self.ipf_graph = IPFGraph()
        else:
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
        
        self.paint_mode = GraphBlock.TEXT_PAINT_MODE
        
        # Current selected arrow
        self.selected_arrow = None
        
        
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
        from_cell = self.ipf_graph.get_block_cell(block.block_name)
        if from_cell is not None and self.ipf_graph.grid_cell_empty(row, column):
            self.ipf_graph.move_block(block.block_name, row, column)
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
        block_name = block.block_name
        block.setParentItem(None)
        self.scene().removeItem(block)
        self.ipf_graph.remove_block(block_name)
        self.graph_blocks.remove(block)
        self.update_connection_arrows()
    
    
    def update_block_positions(self):
        for graph_block in self.graph_blocks:
            row, column = self.ipf_graph.get_block_cell(graph_block.block_name)
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
        iport_prim = None
        oport_prim = None
        if type(port1.ipf_port) == IPort:
            iport_prim = port1
            oport_prim = port2
        else:
            iport_prim = port2
            oport_prim = port1
        
        self.ipf_graph.add_connection(oport_prim.ipf_port, iport_prim.ipf_port)
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
            iport = connection._iport()
            oport = connection._oport()
            iblock_ref = iport._owner_block
            oblock_ref = oport._owner_block
            iport_name = iblock_ref().get_port_name(iport)
            oport_name = oblock_ref().get_port_name(oport)
            iblock_prim = self.get_block_primitive_from_block(iblock_ref)
            oblock_prim = self.get_block_primitive_from_block(oblock_ref)
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
        arrow = GraphGrid.ConnectionArrow(self, begin, end)
        return arrow
    
    
    def block_selected(self, block_primitive):
        """ Notification of block selection change
        
        """
        if self.selected_block is not None:
            self.selected_block.selected = False
            self.selected_block.update()
            
        if self.selected_arrow is not None:
            self.selected_arrow.selected = False
            self.selected_arrow.update()
            
        self.selected_block = block_primitive
        self.selected_block.selected = True
        self.selected_block.update()
        
        graph_block_ref = weakref.ref(block_primitive.parentItem())
        main_form = self.scene().parent()
        main_form.block_selected(graph_block_ref)
    
    
    def connection_arrow_selected(self, arrow):
        """ Notification of connection arrow selected
        
        """
        if self.selected_block is not None:
            self.selected_block.selected = False
            self.selected_block.update() 
        
        if self.selected_arrow is not None:
            self.selected_arrow.selected = False
            self.selected_arrow.update()

        self.selected_arrow = arrow
        self.selected_arrow.selected = True
        self.selected_arrow.update()


    def get_block_primitive_from_block(self, ipf_block_ref):
        for graph_block in self.graph_blocks:
            if ipf_block_ref == graph_block.ipf_block_ref:
                return graph_block
        return None
    
    
    def get_block_cell(self, block_name):
        return self.ipf_graph.get_block_cell(block_name)
    
    
    def get_grid_size(self):
        return self.ipf_graph.get_grid_size()
            
        
    def delete_selected(self):
        if self.selected_block is not None:
            self.remove_block(self.selected_block.parentItem())
            del self.selected_block
            self.selected_block = None

    
    def get_selected_block(self):
        return self.selected_block.parentItem().ipf_block_ref()
    
    
    def load_graph(self, ipf_graph):
        self.selected_block = None
        self.ipf_graph = ipf_graph
        for graph_block in self.graph_blocks:
            graph_block.setParent(None)
            del graph_block
        self.graph_blocks = set()
        for block_name in self.ipf_graph.blocks():
            row, column = self.ipf_graph.get_block_cell(block_name)
            block = graphblock.GraphBlock(
                    weakref.ref(self.ipf_graph.get_block(block_name)), 
                    block_name)
            self.add_block(block, row, column)
        self.update_connection_arrows()
            
    
    def set_block_paint_mode(self, mode):
        self.paint_mode = mode
        for block in self.graph_blocks:
            block.set_paint_mode(mode)
        
    
    def update(self):
        for block in self.graph_blocks:
            block.set_paint_mode(self.paint_mode)
            block.update_preview_image()
    
