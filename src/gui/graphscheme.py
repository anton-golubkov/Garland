# -*- coding: utf-8 -*-


from PySide import QtGui, QtCore

from ipf.ipfgraph import IPFGraph

class GraphScheme( QtGui.QGraphicsScene):
    """ Graph scheme drawing class
    
        This class inherits from QtGui.QGraphicsScene and add functions
        for manage GraphBlocks objects in scheme.
    
    """
    
    def __init__(self ):
        super(GraphScheme, self).__init__()
        gradient = QtGui.QLinearGradient(0, 0, 0, 4000)
        gradient.setColorAt( 0, QtGui.QColor(255, 255, 255))
        gradient.setColorAt( 1, QtGui.QColor(0, 0, 255))
        self.setBackgroundBrush(gradient)
        self._grid = GraphGrid()
        self.addItem(self._grid)
        self._grid.adjust_grid_size()
        self.ipf_graph = IPFGraph()
    
    def add_block(self, block, row, column):
        self.ipf_graph.add_block(block.name, block.block)
        self._grid.add_block(block, row, column)


class GraphGrid(QtGui.QGraphicsRectItem):
    """ Graphics grid class, used in GraphScheme
    
    """
    
    cell_width = 100
    cell_height = 80
    left_margin = 40
    top_margin = 40
    max_width = 20
    max_height = 200
    
    
    def __init__(self, parent=None):
        super(GraphGrid, self).__init__(parent)
        self._grid_width = 5
        self._grid_height = 5
        # Create empty 2-dimension list for blocks in grid
        self._grid_model = [ [None for j in xrange(self.max_width)] \
                             for i in xrange(self.max_height) ]
        self.adjust_grid_size()
        
        # Dummy block used to show dragged block position
        self.dummy_block = QtGui.QGraphicsRectItem(self)
        self.dummy_block.setRect(0, 0, self.cell_width, self.cell_height)
        self.dummy_block.hide()
        
        # Temporary connection arrow
        self.temp_arrow = QtGui.QGraphicsLineItem(self)
        self.temp_arrow.hide() 
        self.temp_arrow.setZValue(20)
        
        
    def paint(self, painter, option, widget):
        pen = painter.pen()
        pen.setColor( QtGui.QColor(200, 200, 200) )
        pen.setWidth(1)
        painter.setPen(pen)
        
        width = self.cell_width * self._grid_width + 2 * self.left_margin
        height = self.cell_height * self._grid_height + 2 * self.top_margin
        for x in range(self.left_margin, width, self.cell_width):
            painter.drawLine(x, 0, x, height)
        for y in range(self.top_margin, height, self.cell_height):
            painter.drawLine(0, y, width, y)
        
        
    def get_grid_size(self):
        """ Get size of graph grid
        
        """
        return (self._grid_width, self._grid_height)
    
    
    def get_cell_in_point(self, point):
        column = int((point[0] - self.left_margin) / self.cell_width)
        row = int((point[1] - self.top_margin) / self.cell_height)
        return (row, column)
    
    
    def adjust_grid_size(self):
        self.setRect(0, 
                     0, 
                     self._grid_width * self.cell_width + 2 * self.left_margin,
                     self._grid_height * self.cell_height + 2 * self.top_margin)
        
    
    def add_block(self, block, row, column):
        """ Add GraphBlock to scheme into specified row and column
        
        """   
        if row < self._grid_height and column < self._grid_width:
            
            if self._grid_model[row][column] is not None:
                # This cell is occupied 
                raise ValueError("Cell (%d, %d) already occupied" % \
                                 (row, column))
            
            self._grid_model[row][column] = block    
            block.setParentItem(self)
            self.update_block_positions()
            
            
        else:
            # Wrong cell address
            raise ValueError("Wrong cell address: (%s, %s); grid size: (%s, %s)" % \
                              (column, row, self._grid_width, self._grid_height))
    
    
    def move_block(self, block, row, column):
        from_cell = self.get_block_cell(block)
        if from_cell is not None and self._grid_model[row][column] is None:
            block_row, block_column = from_cell
            self._grid_model[block_row][block_column] = None
            self._grid_model[row][column] = block
            self.update_block_positions()
            self.disable_dummy_block()
            # Enlarge grid if block moved to last row / column
            if (row == self._grid_height - 1) and self._grid_height < self.max_height:
                self.add_row()
            if (column == self._grid_width - 1) and self._grid_width < self.max_width:
                self.add_column() 
            
    
    def remove_block(self, block):
        row, column = self.get_block_cell(block)
        self._grid_model[row][column] = None
        block.setParentItem(None)
        
    
    def update_block_positions(self):
        for row in range(self._grid_height):
            for column in range(self._grid_width):
                if self._grid_model[row][column] is not None:
                    block = self._grid_model[row][column]
                    x, y = self.get_block_position(block, row, column)
                    block.setPos(x, y)
                    
    
    def get_block_position(self, block, row, column):
        x = self.cell_width * column + self.left_margin
        y = self.cell_height * row + self.top_margin
        shift_x = (self.cell_width - block.rect().width()) / 2
        shift_y = (self.cell_height - block.rect().height()) / 2
        x += shift_x
        y += shift_y
        return (x, y)

    
    def get_block_cell(self, block):
        for row in range(self._grid_height):
            for column in range(self._grid_width):
                if self._grid_model[row][column] == block:
                    return (row, column)
        return None
            
            
    def add_row(self):
        if self.max_height > self._grid_height:
            self._grid_height += 1
            self.adjust_grid_size()
        else:
            raise ValueError("Max row count reached")
       
        
    def add_column(self):
        if self.max_width > self._grid_width:
            self._grid_width += 1
            self.adjust_grid_size()
        else:
            raise ValueError("Max column count reached")
        
    def enable_dummy_block(self):
        self.dummy_block.show()
        
    def disable_dummy_block(self):
        self.dummy_block.hide()
        
    def set_dummy_block_cell(self, row, column):
        if row >= self._grid_height or column >= self._grid_width:
            # Don`t allow move block outside grid
            return
        x, y = self.get_block_position(self.dummy_block, row, column)
        self.dummy_block.setPos(x, y)
        pen = self.dummy_block.pen()
        if self._grid_model[row][column] is not None:
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
        
        